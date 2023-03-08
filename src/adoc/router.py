from fastapi import APIRouter, UploadFile  # , Depends, HTTPException
from typing import List

from src.adoc.schemas import ADOC_S
from src.adoc.services import adoc_get_all_count, adoc_upload_file

router_adoc = APIRouter(
    # prefix="/adoc",
    tags=["Документы"]
)


@router_adoc.get(path='/count',
                 status_code=200,
                 name='Получить количество Документов',
                 tags=['Документы'],
                 description='Получает количество Документов')
async def get_count():
    content = await adoc_get_all_count()
    return content


@router_adoc.post(path="/upload/",
                 status_code=200,
                 name='Загрузить Excel файл',
                 tags=['Документы'],
                 description='Загрузить Excel файл')
async def upload_file(file: UploadFile):
    content = await adoc_upload_file(file)
    return content

# response_model = List[FILES_S],
# @router_files.get(path="/root/{root_folder}",
#                   status_code=200,
#                   name='Получить список Файлов по ROOT_FOLDER',
#                   tags=['Файлы'],
#                   description='Получает список Файлов по конкретной ROOT_FOLDER'
#                   )
# async def get_by_root_folder(root_folder: str):
#     content = await files_get_by_root_folder(root_folder)
#     return content

#
# @router_files.get(path="/search/{str_query}",
#                   status_code=200,
#                   # response_model=List[FILES_S],
#                   name='Получить список Файлов по Запросу',
#                   tags=['Файлы'],
#                   description='Получает список Файлов по Запросу'
#                   )
# async def files_get_fts_by_query(str_query: str):
#     content = await files_get_by_query(str_query)
#     return content

#     return {
#         "status": "success",
#         "data": [dict(result) for result in results],
#         "details": None
#     }
# {
#         "status": "error",
#         "data": None,
#         "details": str(e.__str__())
#     })
