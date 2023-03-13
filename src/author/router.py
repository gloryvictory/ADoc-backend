from fastapi import APIRouter, UploadFile  # , Depends, HTTPException
# from typing import List

from src.adoc.services import adoc_get_all_count, adoc_upload_file, adoc_get_all
from src.author.services import author_get_all_count, author_get_all

router_author = APIRouter(
    # prefix="/adoc",
    tags=["Авторы"]
)


@router_author.get(path='/count',
                 status_code=200,
                 name='Получить количество Авторов',
                 tags=['Авторы'],
                 description='Получает количество Авторов')
async def get_count():
    content = await author_get_all_count()
    return content


@router_author.get(path='/',
                 status_code=200,
                 name='Получить всех Авторов',
                 tags=['Авторы'],
                 description='Получить всех Авторов')
async def get_all():
    content = await author_get_all()
    return content
