from fastapi import APIRouter, UploadFile  # , Depends, HTTPException
# from typing import List

from src.adoc.services import adoc_get_all_count, adoc_upload_file, adoc_get_all, adoc_get_all_by_author, \
    adoc_get_all_by_report, adoc_get_all_by_year, adoc_get_all_by_yeargte, adoc_get_all_by_yearlte, \
    adoc_get_all_by_year_between, adoc_get_all_years, adoc_get_all_with_limit_offset

router_adoc = APIRouter(
    # prefix="/adoc",
    tags=["Документы"]
)


@router_adoc.post(path="/upload/",
                  status_code=200,
                  name='Загрузить Excel файл',
                  tags=['Документы'],
                  description='Загрузить Excel файл')
async def upload_file(file: UploadFile):
    content = await adoc_upload_file(file)
    return content


@router_adoc.get(path='/count',
                 status_code=200,
                 name='Получить количество Документов',
                 tags=['Документы'],
                 description='Получает количество Документов')
async def get_count():
    content = await adoc_get_all_count()
    return content


@router_adoc.get(path='/',
                 status_code=200,
                 name='Получить Документы',
                 tags=['Документы'],
                 description='Получает Документы')
async def get_all():
    content = await adoc_get_all()
    return content

@router_adoc.get(path='/{limit}/{offset}',
                 status_code=200,
                 name='Получить Документы с указанием количества',
                 tags=['Документы'],
                 description='Получает Документы с указанием количества')
async def get_all(limit:int, offset:int):
    content = await adoc_get_all_with_limit_offset(limit, offset)
    return content


@router_adoc.get(path='/author/{author}',
                 status_code=200,
                 name='Получить Документы по автору',
                 tags=['Документы'],
                 description='Получает Документы по автору')
async def get_all_by_author(author: str):
    content = await adoc_get_all_by_author(author)
    return content


@router_adoc.get(path='/report/{report}',
                 status_code=200,
                 name='Получить Документы по отчету',
                 tags=['Документы'],
                 description='Получает Документы по отчету')
async def get_all_by_author(report: str):
    content = await adoc_get_all_by_report(report)
    return content


@router_adoc.get(path='/year/{year}',
                 status_code=200,
                 name='Получить Документы по году',
                 tags=['Документы'],
                 description='Получает Документы по году')
async def get_all_by_author(year: int):
    content = await adoc_get_all_by_year(year)
    return content


@router_adoc.get(path='/year_gte/{year}',
                 status_code=200,
                 name='Получить Документы больше года',
                 tags=['Документы'],
                 description='Получает Документы больше года')
async def get_all_by_year_gte(year: int):
    content = await adoc_get_all_by_yeargte(year)
    return content


@router_adoc.get(path='/year_lte/{year}',
                 status_code=200,
                 name='Получить Документы меньше года',
                 tags=['Документы'],
                 description='Получает Документы меньше года')
async def get_all_by_year_lte(year: int):
    content = await adoc_get_all_by_yearlte(year)
    return content


@router_adoc.get(path='/year_between/{year1}/{year2}',
                 status_code=200,
                 name='Получить Документы между годами',
                 tags=['Документы'],
                 description='Получает Документы между годами')
async def get_all_by_year_between(year1: int, year2: int):
    content = await adoc_get_all_by_year_between(year1, year2)
    return content

@router_adoc.get(path='/year',
                 status_code=200,
                 name='Получить все уникальные года',
                 tags=['Документы'],
                 description='Получает  все уникальные года')
async def get_all_by_years():
    content = await adoc_get_all_years()
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
