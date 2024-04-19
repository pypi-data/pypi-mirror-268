"""
The HEA Trash Microservice provides deleted file management.
"""

import asyncio
from functools import partial
import itertools
from heaserver.service import response
from heaobject.data import AWSS3FileObject
from heaobject.folder import AWSS3Folder
from heaobject.trash import AWSS3FolderFileTrashItem
from heaobject.awss3key import decode_key, encode_key, KeyDecodeException, is_folder, display_name
from heaobject.user import NONE_USER
from heaobject.root import DesktopObjectDict
from heaserver.service.runner import init_cmd_line, routes, start, web
from heaserver.service.db import awsservicelib
from heaserver.service.db.aws import S3Manager
from heaserver.service.wstl import builder_factory, action
from heaserver.service.appproperty import HEA_DB, HEA_BACKGROUND_TASKS
from heaserver.service.oidcclaimhdrs import SUB
from heaserver.service.sources import AWS_S3
from heaserver.service.wstl import action
from aiohttp import web, hdrs
import logging
from typing import Any, AsyncGenerator, AsyncIterator, Union
from multidict import istr
from mypy_boto3_s3 import S3Client
from mypy_boto3_s3.type_defs import ListObjectVersionsOutputTypeDef
from botocore.exceptions import ClientError
from yarl import URL
from datetime import datetime, timezone
from operator import itemgetter
from aiostream import stream
from heaserver.service.customhdrs import PREFER, PREFERENCE_RESPOND_ASYNC
from concurrent.futures import ProcessPoolExecutor
import os


TRASHAWSS3_COLLECTION = 'awss3trashitems'
MAX_VERSIONS_TO_RETRIEVE = 50000


_status_id = 0


@routes.get('/ping')
async def ping(request: web.Request) -> web.Response:
    """
    For testing whether the service is up.

    :param request: the HTTP request.
    :return: Always returns status code 200.
    """
    return response.status_ok()


@routes.route('OPTIONS', '/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
async def get_item_options(request: web.Request) -> web.Response:
    """
    Gets the allowed HTTP methods for a trash item.

    :param request: a HTTP request (required).
    :return: the HTTP response.
    ---
    summary: Allowed HTTP methods.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        description: Expected response to a valid request.
        content:
            text/plain:
                schema:
                    type: string
                    example: "200: OK"
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        resp = await _get_deleted_item(request)
        if resp is not None:
            return await response.get_options(request, ['GET', 'HEAD', 'OPTIONS'])
        else:
            return response.status_not_found()
    except web.HTTPError as e:
        headers: dict[Union[str, istr], str] = {
            hdrs.CONTENT_TYPE: 'text/plain; charset=utf-8'}
        return response.status_generic(status=e.status, body=e.text, headers=headers)


@routes.route('OPTIONS', '/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/opener')
async def get_item_opener_options(request: web.Request) -> web.Response:
    """
    Gets the allowed HTTP methods for a trash item opener.

    :param request: a HTTP request (required).
    :return: the HTTP response.
    ---
    summary: Allowed HTTP methods.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        description: Expected response to a valid request.
        content:
            text/plain:
                schema:
                    type: string
                    example: "200: OK"
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        resp = await _get_deleted_item(request)
        if resp is not None:
            if is_folder(resp['key']):
                return await response.get_options(request, ['GET', 'HEAD', 'OPTIONS'])
            else:
                return await response.get_options(request, ['OPTIONS'])
        else:
            return response.status_not_found()
    except web.HTTPError as e:
        headers: dict[Union[str, istr], str] = {
            hdrs.CONTENT_TYPE: 'text/plain; charset=utf-8'}
        return response.status_generic(status=e.status, body=e.text, headers=headers)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
@action(name='heaserver-awss3trash-item-get-open-choices',
        rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/opener',
        itemif='actual_object_type_name == "heaobject.folder.AWSS3Folder"')
@action(name='heaserver-awss3trash-item-get-properties',
        rel='hea-properties hea-context-menu')
@action('heaserver-awss3trash-item-restore',
        rel='hea-trash-restore-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/restorer')
@action('heaserver-awss3trash-item-permanently-delete',
        rel='hea-trash-delete-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/deleter')
@action('heaserver-awss3trash-item-get-self', rel='self',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
@action('heaserver-awss3trash-item-get-volume',
        rel='hea-volume',
        path='volumes/{volume_id}')
@action('heaserver-awss3trash-item-get-awsaccount',
        rel='hea-account',
        path='volumes/{volume_id}/awsaccounts/me')
async def get_deleted_item(request: web.Request) -> web.Response:
    """
    Gets a delete item.

    :param request: the HTTP request.
    :return the deleted item in a list, or Not Found.
    ---
    summary: A deleted item.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    sub = request.headers.get(SUB, NONE_USER)
    result = await _get_deleted_item(request)
    if result is None:
        return await response.get(request, None)
    else:
        return await response.get(request, result.to_dict(), permissions=result.get_permissions(sub))


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trashfolders/{trash_folder_id}/items/')
@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trashfolders/{trash_folder_id}/items')
@action(name='heaserver-awss3trash-item-get-open-choices',
        rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/opener',
        itemif='actual_object_type_name == "heaobject.folder.AWSS3Folder"')
@action(name='heaserver-awss3trash-item-get-properties',
        rel='hea-properties hea-context-menu')
@action('heaserver-awss3trash-item-restore',
        rel='hea-trash-restore-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/restorer')
@action('heaserver-awss3trash-item-permanently-delete',
        rel='hea-trash-delete-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/deleter')
@action('heaserver-awss3trash-item-get-self', rel='self',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
async def get_items_in_trash_folder(request: web.Request) -> web.Response:
    """
    Gets a list of all deleted items in a volume, bucket, and trash folder. It
    only retrieves items with the folder as a parent, not including any
    subfolders.

    :param request: the HTTP request.
    :return: the list of items with delete markers in the requested folder, or
    Not Found.
    ---
    summary: Gets a list of the deleted items from the given folder.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - name: trash_folder_id
          in: path
          required: true
          description: The id of the trash folder to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A trash folder id
              value: root
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    sub = request.headers.get(SUB, NONE_USER)
    result: list[AWSS3FolderFileTrashItem] = []
    async for i in _get_deleted_items(request, recursive=False):
        result.append(i)
    return await response.get_all(request, tuple(r.to_dict() for r in result), permissions=tuple(r.get_permissions(sub) for r in result))


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3folders/{folder_id}/awss3trash/')
@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3folders/{folder_id}/awss3trash')
@action(name='heaserver-awss3trash-item-get-open-choices',
        rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/opener',
        itemif='actual_object_type_name == "heaobject.folder.AWSS3Folder"')
@action(name='heaserver-awss3trash-item-get-properties',
        rel='hea-properties hea-context-menu')
@action('heaserver-awss3trash-item-restore',
        rel='hea-trash-restore-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/restorer')
@action('heaserver-awss3trash-item-permanently-delete',
        rel='hea-trash-delete-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/deleter')
@action('heaserver-awss3trash-item-get-self', rel='self',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
async def get_deleted_items_in_folder(request: web.Request) -> web.Response:
    """
    Gets a list of all deleted items in a volume, bucket, and folder. It only
    retrieves items with the folder as a parent, not including any subfolders.

    :param request: the HTTP request.
    :return: the list of items with delete markers or the requested bucket, or
    Not Found.
    ---
    summary: Gets a list of the deleted items from the given folder.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - name: folder_id
          in: path
          required: true
          description: The id of the folder to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A folder id
              value: root
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    sub = request.headers.get(SUB, NONE_USER)
    result: list[AWSS3FolderFileTrashItem] = []
    async for i in _get_deleted_items(request, recursive=False):
        result.append(i)
    return await response.get_all(request, tuple(r.to_dict() for r in result), permissions=tuple(r.get_permissions(sub) for r in result))


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/')
@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trash')
@action(name='heaserver-awss3trash-item-get-open-choices',
        rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/opener',
        itemif='isheaobject(heaobject.folder.AWSS3Folder)')
@action('heaserver-awss3trash-item-get-properties',
        rel='hea-properties hea-context-menu')
@action('heaserver-awss3trash-item-restore',
        rel='hea-trash-restore-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/restorer')
@action('heaserver-awss3trash-item-permanently-delete',
        rel='hea-trash-delete-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/deleter')
@action('heaserver-awss3trash-item-get-self', rel='self',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
@action('heaserver-awss3trash-do-empty-trash', rel='hea-trash-emptier',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trashemptier')
async def get_all_deleted_items(request: web.Request) -> web.Response:
    """
    Gets a list of all deleted items in a volume and bucket.

    :param request: the HTTP request.
    :return: the list of items with delete markers or the requested bucket, Not
    Found.
    ---
    summary: Gets a list of all deleted items.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to check for deleted files.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    async def coro():
        result: list[AWSS3FolderFileTrashItem] = []
        async for i in _get_deleted_items(request):
            result.append(i)
        return await response.get_all(request, tuple(r.to_dict() for r in result),
                                      permissions=tuple(r.get_permissions(sub) for r in result))
    async_requested = PREFERENCE_RESPOND_ASYNC in request.headers.get(PREFER, [])
    if async_requested:
        logger.debug('Asynchronous get all trash')
        global _status_id
        status_location = f'{str(request.url).rstrip("/")}asyncstatus{_status_id}'
        _status_id += 1
        task_name = f'{sub}^{status_location}'
        await request.app[HEA_BACKGROUND_TASKS].add(coro(), task_name)
        return response.status_see_other(status_location)
    else:
        logger.debug('Synchronous get all trash')
        return await coro()




@routes.get('/volumes/{volume_id}/awss3trash/')
@routes.get('/volumes/{volume_id}/awss3trash')
@action(name='heaserver-awss3trash-item-get-open-choices',
        rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/opener',
        itemif='isheaobject(heaobject.folder.AWSS3Folder)')
@action('heaserver-awss3trash-item-get-properties',
        rel='hea-properties hea-context-menu')
@action('heaserver-awss3trash-item-restore',
        rel='hea-trash-restore-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/restorer')
@action('heaserver-awss3trash-item-permanently-delete',
        rel='hea-trash-delete-confirmer hea-context-menu hea-confirm-prompt',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/deleter')
@action('heaserver-awss3trash-item-get-self', rel='self',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
@action('heaserver-awss3trash-do-empty-trash', rel='hea-trash-emptier',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trashemptier')
async def get_all_deleted_items_all_buckets(request: web.Request) -> web.Response:
    """
    Gets a list of all deleted items in a volume.

    :param request: the HTTP request.
    :return: the list of items with delete markers.
    ---
    summary: Gets a list of all deleted items.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to check for deleted files.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        volume_id = request.match_info['volume_id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    s3: S3Client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    loop = asyncio.get_running_loop()
    resp_ = await loop.run_in_executor(None, s3.list_buckets)

    async def coro() -> web.Response:
        asyncgens: list[AsyncGenerator[AWSS3FolderFileTrashItem, None]] = []
        try:
            for bucket in resp_.get('Buckets', []):
                async def asyncgen(volume_id: str, bucket_id: str, sub: str | None) -> AsyncGenerator[AWSS3FolderFileTrashItem, None]:
                    async for item in _get_deleted_items_private(s3, volume_id, bucket_id, None, sub):
                        yield item
                asyncgens.append(asyncgen(request.match_info['volume_id'], bucket['Name'], request.headers.get(SUB)))
            async with stream.merge(*asyncgens).stream() as streamer:
                result: list[AWSS3FolderFileTrashItem] = []
                async for item in streamer:
                    result.append(item)
                return await response.get_all(request, tuple(r.to_dict() for r in result),
                                              permissions=tuple(r.get_permissions(sub) for r in result))
        except ValueError as e:
            return response.status_forbidden(str(e))
    async_requested = PREFERENCE_RESPOND_ASYNC in request.headers.get(PREFER, [])
    if async_requested:
        logger.debug('Asynchronous get all trash')
        global _status_id
        status_location = f'{str(request.url).rstrip("/")}asyncstatus{_status_id}'
        _status_id += 1
        task_name = f'{sub}^{status_location}'
        await request.app[HEA_BACKGROUND_TASKS].add(coro(), task_name)
        return response.status_see_other(status_location)
    else:
        logger.debug('Synchronous get all trash')
        return await coro()

@routes.get('/volumes/{volume_id}/awss3trashasyncstatus{status_id}')
@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trashasyncstatus{status_id}')
async def get_trash_async_status(request: web.Request) -> web.Response:
    return response.get_async_status(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trashemptier')
async def do_empty_trash(request: web.Request) -> web.Response:
    """
    Empties a version-enabled bucket's trash.

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Empties the bucket's trash.
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _do_empty_trash(request)


@routes.delete('/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}')
async def permanently_delete_object_with_delete(request: web.Request) -> web.Response:
    """
    Delete all versions of a version enabled file

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Permanent file deletion
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume containing file.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to containing file.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _permanently_delete_object(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/deleter')
async def permanently_delete_object(request: web.Request) -> web.Response:
    """
    Delete all versions of a version enabled file

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Permanent file deletion
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume containing file.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to containing file.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _permanently_delete_object(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/restorer')
async def restore_object(request: web.Request) -> web.Response:
    """
    Removes the delete marker for a specified file

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: File deletion
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _undelete_object(request)



@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3trash/{id}/opener')
@action('heaserver-awss3trash-item-open-default',
        rel='hea-opener hea-default application/x.item',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3trashfolders/{id}/items/',
        itemif='isheaobject(heaobject.folder.AWSS3Folder)')
async def get_trash_item_opener(request: web.Request) -> web.Response:
    """
    Opens the requested trash forder.

    :param request: the HTTP request. Required.
    :return: the opened folder, or Not Found if the requested item does not exist.
    ---
    summary: Folder opener choices
    tags:
        - heaserver-trash-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '300':
        $ref: '#/components/responses/300'
      '404':
        $ref: '#/components/responses/404'
    """
    sub = request.headers.get(SUB, NONE_USER)
    result = await _get_deleted_item(request)
    if result is None:
        return await response.get_multiple_choices(request, None)
    else:
        return await response.get_multiple_choices(request, result.to_dict(), permissions=result.get_permissions(sub))


def main() -> None:
    config = init_cmd_line(description='Deleted file management',
                           default_port=8080)
    start(package_name='heaserver-trash-aws-s3', db=S3Manager,
          wstl_builder_factory=builder_factory(__package__), config=config)


async def _get_version_objects(s3: S3Client, bucket_id: str, prefix: str,
                              loop: asyncio.AbstractEventLoop | None = None) -> AsyncIterator[ListObjectVersionsOutputTypeDef]:
    if not loop:
        loop_ = asyncio.get_running_loop()
    else:
        loop_ = loop
    try:
        paginator = s3.get_paginator('list_object_versions')
        paginate_partial = partial(paginator.paginate, Bucket=bucket_id)
        if prefix is not None:
            paginate_partial = partial(paginate_partial, Prefix=prefix)
        for page in await loop_.run_in_executor(None, paginate_partial):
            yield page
    except ClientError as e:
        raise awsservicelib.handle_client_error(e)



async def _get_deleted_item(request: web.Request) -> AWSS3FolderFileTrashItem | None:
    try:
        volume_id = request.match_info['volume_id']
        bucket_id = request.match_info['bucket_id']
    except KeyError as e:
        raise response.status_bad_request(str(e))
    try:
        item = AWSS3FolderFileTrashItem()
        item.id = request.match_info['id']
        key_ = item.key
        s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    except ValueError as e:
        return None
    async for deleted_item in _get_deleted_items_private(s3, volume_id, bucket_id, key_, request.headers.get(SUB), version=item.version, recursive=False):
        return deleted_item
    return None


async def _get_deleted_items(request: web.Request, recursive=True) -> AsyncIterator[AWSS3FolderFileTrashItem]:
    """
    Gets all deleted items (with a delete marker) in a volume and bucket.
    The request's match_info is expected to have volume_id and bucket_id keys
    containing the volume id and bucket name, respectively. It can optionally
    contain a folder_id or trash_folder_id, which will restrict returned items
    to a folder or trash folder, respectively.

    :param request: the HTTP request (required).
    :return: an asynchronous iterator of AWSS3FolderFileItems.
    :raises HTTPBadRequest: if the request doesn't have a volume id or bucket
    name.
    """
    try:
        volume_id = request.match_info['volume_id']
        bucket_id = request.match_info['bucket_id']
    except KeyError as e:
        raise response.status_bad_request(str(e))
    folder_id = request.match_info.get('folder_id', None)
    trash_folder_id = request.match_info.get('trash_folder_id', None)
    try:
        if folder_id:
            prefix: str | None = decode_key(folder_id) if folder_id != 'root' else ''
        elif trash_folder_id:
            if trash_folder_id != 'root':
                item = AWSS3FolderFileTrashItem()
                item.id = trash_folder_id
                prefix = item.key
            else:
                prefix = ''
        else:
            prefix = None
    except (KeyDecodeException, ValueError) as e:
        raise response.status_not_found()

    try:
        s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    except ValueError:
        raise response.status_not_found()

    async for item in _get_deleted_items_private(s3, volume_id, bucket_id, prefix, request.headers.get(SUB), recursive=recursive):
        yield item

#count = 0
def _process_resp(volume_id: str, bucket_id: str, sub_user: str | None, version: str | None, recursive: bool, response_) -> list[AWSS3FolderFileTrashItem]:
    logger = logging.getLogger(__name__)
    # count += len(response_.get('Versions', []))
    # if count > MAX_VERSIONS_TO_RETRIEVE:
    #     raise ValueError(f'The bucket {bucket_id} has too many objects to display the trash!')
    result: list[AWSS3FolderFileTrashItem] = []
    def truncate(key: str):
        try:
            return key[:key.index('/') + 1]
        except ValueError:
            return key
    if not recursive:
        truncated_key_dict: dict[str, AWSS3FolderFileTrashItem] = {}
    timezone_aware_min = datetime.min.replace(tzinfo=timezone.utc)
    delete_markers = {item['Key']: item['LastModified'] for item in response_.get('DeleteMarkers', []) if item['IsLatest']}
    if not delete_markers:
        return []
    logger.debug('delete_markers: %s', delete_markers)
    # Assume the data coming from AWS is already sorted by Key.
    def version_iter(r, dms):
        # This function is necessary due to python's late binding closures. We need it to bind to the right
        # response_ and delete_markers objects.
        return (vers for vers in r.get('Versions', [])
                    if vers['VersionId'] != 'null' and
                    vers['VersionId'] is not None and
                    (version is None or version == vers['VersionId']) and
                    vers['Key'] in dms)
    non_null_versions = version_iter(response_, delete_markers)
    for key, versions in itertools.groupby(non_null_versions, itemgetter('Key')):
        if not recursive:
            if key not in truncated_key_dict.keys():
                for item in truncated_key_dict.values():
                    result.append(item)
                truncated_key_dict.clear()
        # Versions are returned by S3 in the order in which they are stored, with the most recently stored returned
        # first.
        version_ = next(v for v in versions if v['LastModified'] < delete_markers[key])
        logger.debug('Version response for key %s and version %s', key, version_)
        if version_:
            deleted = delete_markers[key]
            key = key if recursive else truncate(key)
            encoded_key = encode_key(key)
            last_modified = version_['LastModified']
            storage_class = version_['StorageClass']
            size = version_['Size']
            if recursive:
                item = AWSS3FolderFileTrashItem()
            else:
                item = truncated_key_dict.setdefault(key, AWSS3FolderFileTrashItem())
            item.bucket_id = bucket_id
            item.key = key
            item.version = version_['VersionId']
            item.modified = last_modified if recursive else max(item.modified or timezone_aware_min, last_modified)
            item.created = last_modified if recursive else max(item.modified or timezone_aware_min, last_modified)
            item.deleted = deleted
            item.owner = (sub_user if sub_user is not None else NONE_USER) if recursive else None
            item.volume_id = volume_id
            item.source = AWS_S3
            item.storage_class = storage_class if recursive else None
            item.size = size if recursive else (item.size or 0) + size
            item.actual_object_type_name = AWSS3Folder.get_type_name() \
                if is_folder(key) else AWSS3FileObject.get_type_name()
            if is_folder(key):
                item.actual_object_uri = str(
                    URL('volumes') / volume_id / 'buckets' / bucket_id / 'awss3folders' / encoded_key)
            else:
                item.actual_object_uri = str(
                    URL('volumes') / volume_id / 'buckets' / bucket_id / 'awss3files' / encoded_key)
            if recursive:
                result.append(item)
    if not recursive:
        for item in truncated_key_dict.values():
            result.append(item)
    return result


from collections.abc import Callable
from typing import TypeVar
T = TypeVar('T')
U = TypeVar('U')
async def _queued_processing(producer: Callable[[], AsyncGenerator[T, None]],
                             consumer: Callable[[T], AsyncGenerator[U, None]],
                             exceptions_to_ignore: Callable[[Exception], bool] | None = None,
                             queue_max_size=100, num_workers=10) -> AsyncGenerator[U, None]:
    """
    Places items in an async generator into an asyncio queue for processing by the provided async item_processor.
    Specified exceptions may be suppressed.

    :param generator: the item async generator (required).
    :param item_processor: the async item processor.
    :param exceptions_to_ignore: a function that takes an exception parameter and returns whether the exception should
    be suppressed.
    :param queue_max_size the maximum size of the queue (default is 0, meaning infinite size).
    :param num_workers: the number of workers that take items off the queue (default is 10).
    """
    logger = logging.getLogger(__name__)
    queue: asyncio.Queue[T] = asyncio.Queue(queue_max_size)
    async def worker(name: str, queue: asyncio.Queue) -> list[U]:
        result: list[U] = []
        try:
            logger.debug('Starting worker %s', name)
            while True:
                coro = await queue.get()
                logger.debug('Worker %s processing item %s', name, coro)
                try:
                    async for item in consumer(coro):
                        result.append(item)
                    logger.debug('Worker %s processing item %s', name, coro)
                finally:
                    queue.task_done()
        except asyncio.CancelledError:
            logger.debug('Ending worker %s', name)
            return result
        except:
            logger.exception('Error in worker %s', name)
            raise
    workers: list[asyncio.Task[list[U]]] = []
    for i in range(num_workers):
        workers.append(asyncio.create_task(worker(f'worker-{i}', queue)))
    try:
        async for coro in producer():
            await queue.put(coro)
        await queue.join()
    finally:
        for worker_ in workers:
            worker_.cancel()
        exceptions_to_raise = []
        for result in asyncio.as_completed(workers):
            result_ = await result
            if isinstance(result_, Exception) and (not exceptions_to_ignore or not exceptions_to_ignore(result_)):
                exceptions_to_raise.append(result_)
            else:
                for r_ in result_:
                    yield r_
        if exceptions_to_raise:
            raise exceptions_to_raise[0]


async def _get_deleted_items_private(s3: S3Client, volume_id: str, bucket_id: str, prefix: str | None = None,
                                       sub_user: str | None = None, version: str | None = None, recursive=True) -> AsyncGenerator[AWSS3FolderFileTrashItem, None]:
    logger = logging.getLogger(__name__)
    loop_ = asyncio.get_running_loop()
    cpu_count = os.cpu_count()
    max_workers = int((cpu_count if cpu_count else 2) / 2)
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        async def producer() -> AsyncGenerator[asyncio.Future[list[AWSS3FolderFileTrashItem]], None]:
            async for response_ in _get_version_objects(s3, bucket_id, prefix if prefix else '', loop_):
                yield loop_.run_in_executor(pool, _process_resp, volume_id, bucket_id, sub_user, version, recursive, response_)

        async def consumer(item: asyncio.Future[list[AWSS3FolderFileTrashItem]]) -> AsyncGenerator[AWSS3FolderFileTrashItem, None]:
            await item
            for result in item.result():
                yield result

        async for result in _queued_processing(producer, consumer):
            yield result


async def _undelete_object(request: web.Request) -> web.Response:
    """
    Undeletes a versioned file that was deleted by removing the file's active
    delete marker. A versioned file presents as deleted when its latest version
    is a delete marker. By removing the delete marker, we make the previous
    version the latest version and the file then presents as *not* deleted.

    The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id
    entry of the request's match_info dictionary. The file id must be in the id
    entry of the request's match_info dictionary.

    :param request: the aiohttp Request (required).
    :return: the HTTP response with a 204 status code if the file was
    successfully deleted, 403 if access was denied, 404 if the file was not
    found, 405 if delete marker doesn't have the latest modified time or 500 if
    an internal error occurred.
    """
    try:
        volume_id = request.match_info['volume_id']
        bucket_name = request.match_info['bucket_id']
        item = AWSS3FolderFileTrashItem()
        item.id = request.match_info['id']
        key_ = item.key
    except KeyError as e:
        return response.status_bad_request(f'{e} is required')
    except KeyDecodeException as e:
        return response.status_bad_request(f'{e}')

    loop = asyncio.get_running_loop()

    try:
        if not await _get_deleted_item(request):
            return response.status_not_found(f'Object {display_name(key_)} is not in the trash')
        s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
        async for response_ in _get_version_objects(s3_client, bucket_name, key_, loop):
            keyfunc = lambda x: x['Key']

            # Preflight
            for key, versions in itertools.groupby(sorted((resp for resp in itertools.chain((vers for vers in response_['DeleteMarkers'] if vers['VersionId'] != 'null'), (vers for vers in response_.get('Versions', []) if vers['VersionId'] != 'null'))), key=keyfunc), key=keyfunc):
                resps = sorted(versions, key=lambda x: x['LastModified'], reverse=True)
                if resps and 'Size' in resps[0]:
                    if not is_folder(resps[0]['Key']):
                        return response.status_bad_request(f'Object {display_name(key)} has been overwritten')

            # Actual
            for key, versions in itertools.groupby(sorted((resp for resp in itertools.chain((vers for vers in response_['DeleteMarkers'] if vers['VersionId'] != 'null'), (vers for vers in response_.get('Versions', []) if vers['VersionId'] != 'null'))), key=keyfunc), key=keyfunc):
                resps = sorted(versions, key=lambda x: x['LastModified'], reverse=True)
                for resp_ in resps:
                    if 'Size' not in resp_:  # Delete the delete markers until we reach actual version objects.
                        s3_client.delete_object(Bucket=bucket_name, Key=resp_['Key'], VersionId=resp_['VersionId'])
                    else:
                        break

    except ClientError as e:
        return awsservicelib.handle_client_error(e)

    return response.status_no_content()


# async def rollback_file(request: web.Request) -> web.Response:
#     """
#     Makes the specified version the current version by deleting all recent versions
#     The volume id must be in the volume_id entry of the
#     request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
#     dictionary. The file id must be in the id entry of the request's match_info dictionary.
#     And the version_id must be in the version id entry of the request's match_info dictionary.

#     :param request: the aiohttp Request (required).
#     :return: the HTTP response with a 204 status code if the file was successfully deleted, 403 if access was denied,
#     404 if the file was not found, 405 if delete marker doesn't have the latest modified time or 500 if an internal error occurred.
#     """
#     logger = logging.getLogger(__name__)

#     if 'volume_id' not in request.match_info:
#         return response.status_bad_request('volume_id is required')
#     if 'bucket_id' not in request.match_info:
#         return response.status_bad_request('bucket_id is required')
#     if 'id' not in request.match_info and 'name' not in request.match_info:
#         return response.status_bad_request('either id or name is required')
#     if 'version_id' not in request.match_info:
#         return response.status_bad_request('version_id is required')

#     volume_id = request.match_info['volume_id']
#     bucket_name = request.match_info['bucket_id']
#     file_name = request.match_info['id'] if 'id' in request.match_info else request.match_info['name']
#     version_id = request.match_info['version_id']

#     loop = asyncio.get_running_loop()

#     try:
#         s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)

#         # Get the latest version for the object.
#         vresponse = await loop.run_in_executor(None, partial(s3_client.meta.client.list_object_versions(Bucket=bucket_name, Prefix=file_name)))

#         if version_id in [ver['VersionId'] for ver in vresponse['Versions']]:
#             for version in vresponse['Versions']:
#                 if (version['VersionId'] != version_id) and (version['Key'] == file_name):
#                     s3_client.ObjectVersion(
#                         bucket_name, file_name, version['VersionId']).delete()
#                 else:
#                     break

#         else:
#             return response.status_bad_request(f"{version_id} was not found in the list of versions for "f"{file_name}.")

#     except ClientError as e:
#         return awsservicelib.handle_client_error(e)

#     return await get_file(request)


# async def rollforward_file(request: web.Request) -> web.Response:
#     """
#     Makes the specified version the current version by deleting all recent versions
#     The volume id must be in the volume_id entry of the
#     request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
#     dictionary. The file id must be in the id entry of the request's match_info dictionary.
#     And the version_id must be in the version id entry of the request's match_info dictionary.

#     :param request: the aiohttp Request (required).
#     :return: the HTTP response with a 204 status code if the file was successfully deleted, 403 if access was denied,
#     404 if the file was not found, 405 if delete marker doesn't have the latest modified time or 500 if an internal error occurred.
#     """
#     logger = logging.getLogger(__name__)

#     if 'volume_id' not in request.match_info:
#         return response.status_bad_request('volume_id is required')
#     if 'bucket_id' not in request.match_info:
#         return response.status_bad_request('bucket_id is required')
#     if 'id' not in request.match_info and 'name' not in request.match_info:
#         return response.status_bad_request('either id or name is required')
#     if 'version_id' not in request.match_info:
#         return response.status_bad_request('version_id is required')

#     volume_id = request.match_info['volume_id']
#     bucket_name = request.match_info['bucket_id']
#     file_name = request.match_info['id'] if 'id' in request.match_info else request.match_info['name']
#     version_id = request.match_info['version_id']

#     loop = asyncio.get_running_loop()

#     try:
#         s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)

#         # copy the specified version into the file
#         copy_source = {'Bucket': bucket_name,
#                        'Key': file_name, 'VersionId': version_id}

#         s3_client.meta.client.copy_object(
#             CopySource=copy_source, Bucket=bucket_name, Key=file_name)

#         # delete the original version
#         s3_client.ObjectVersion(bucket_name, file_name, version_id).delete()

#     except ClientError as e:
#         return awsservicelib.handle_client_error(e)

#     return await get_file(request)


async def _permanently_delete_object(request: web.Request) -> web.Response:
    """
    Makes the specified version the current version by deleting all recent versions
    The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
    dictionary. The file id must be in the id entry of the request's match_info dictionary.
    And the version_id must be in the version id entry of the request's match_info dictionary.

    :param request: the aiohttp Request (required).
    :return: the HTTP response with a 204 status code if the file was successfully deleted, 403 if access was denied,
    404 if the file was not found, 405 if delete marker doesn't have the latest modified time or 500 if an internal error occurred.
    """
    logger = logging.getLogger(__name__)

    try:
        volume_id = request.match_info['volume_id']
        bucket_name = request.match_info['bucket_id']
        item = AWSS3FolderFileTrashItem()
        item.id = request.match_info['id']
        key = item.key
        version = item.version
    except KeyError as e:
        return response.status_bad_request(f'{e} is required')
    except (ValueError, KeyDecodeException) as e:
        return response.status_not_found()

    loop = asyncio.get_running_loop()

    try:
        s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
        async for response_ in _get_version_objects(s3_client, bucket_name, key, loop):
            delete_markers_to_delete = []
            versions_to_delete = []
            delete_marker = False
            for resp_ in sorted((resp for resp in itertools.chain((vers for vers in response_.get('DeleteMarkers', []) if vers['VersionId'] != 'null'), (vers for vers in response_.get('Versions', []) if vers['VersionId'] != 'null')) if resp['Key'] == key), key=lambda x: x['LastModified'], reverse=True):
                if not delete_marker and resp_['VersionId'] == version:
                    delete_marker = True
                    delete_markers_to_delete.append(resp_)
                    continue
                if delete_marker and 'Size' not in resp_ and versions_to_delete:
                    delete_marker = False
                    break
                if 'Size' not in resp_:
                    delete_markers_to_delete.append(resp_)
                else:
                    versions_to_delete.append(resp_)
            if not delete_markers_to_delete:
                return response.status_not_found(f'Object {display_name(key)} is not in the trash')
            for version_to_delete in itertools.chain(versions_to_delete, delete_markers_to_delete):
                s3_client.delete_object(Bucket=bucket_name, Key=key, VersionId=version_to_delete['VersionId'])
    except ClientError as e:
        return awsservicelib.handle_client_error(e)

    return response.status_no_content()


async def _do_empty_trash(request: web.Request) -> web.Response:
    """
    Makes the specified version the current version by deleting all recent versions
    The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
    dictionary. The file id must be in the id entry of the request's match_info dictionary.
    And the version_id must be in the version id entry of the request's match_info dictionary.

    :param request: the aiohttp Request (required).
    :return: the HTTP response with a 204 status code if the file was successfully deleted, 403 if access was denied,
    404 if the file was not found, 405 if delete marker doesn't have the latest modified time or 500 if an internal error occurred.
    """
    logger = logging.getLogger(__name__)

    try:
        volume_id = request.match_info['volume_id']
        bucket_name = request.match_info['bucket_id']
    except KeyError as e:
        return response.status_bad_request(f'{e} is required')

    loop = asyncio.get_running_loop()

    try:
        s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
        async for response_ in _get_version_objects(s3_client, bucket_name, None, loop):
            keyfunc = lambda x: x['Key']
            for key, versions in itertools.groupby(sorted((resp for resp in itertools.chain((vers for vers in response_.get('DeleteMarkers', []) if vers['VersionId'] != 'null'), (vers for vers in response_.get('Versions', []) if vers['VersionId'] != 'null'))), key=keyfunc), key=keyfunc):
                delete_markers_to_delete = []
                versions_to_delete = []
                delete_markers = True
                for resp_ in sorted((resp for resp in versions), key=lambda x: x['LastModified'], reverse=True):
                    if delete_markers and 'Size' not in resp_:
                        delete_markers_to_delete.append(resp_)
                    elif 'Size' in resp_ and delete_markers_to_delete:
                        delete_markers = False
                        versions_to_delete.append(resp_)
                    else:
                        break
                for version_to_delete in itertools.chain(versions_to_delete, delete_markers_to_delete):
                    s3_client.delete_object(Bucket=bucket_name, Key=key, VersionId=version_to_delete['VersionId'])
    except ClientError as e:
        return awsservicelib.handle_client_error(e)

    return response.status_no_content()
