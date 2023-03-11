from fastapi import UploadFile, File
import os
from src import cfg
from src.adoc.models import ADOC_M, ADOC_HISTORY_M
import openpyxl


# import asyncpg


async def adoc_get_all_count():
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_count = await ADOC_M.objects.count()
        # log.info(f"count load successfuly: {all_count}")
        content = {"msg": "Success", "count": all_count}
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {ADOC_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content


async def adoc_upload_file(file: UploadFile = File(...)):
    content = {"msg": f"Unknown error"}
    try:

        if not os.path.isdir(cfg.FOLDER_UPLOAD):
            os.mkdir(cfg.FOLDER_UPLOAD)
        file_in = file.filename
        file_out = file.filename.replace(" ", "-")

        file_name = os.path.join(os.getcwd(), cfg.FOLDER_UPLOAD, file_out)

        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} - deleted !")

        contents = file.file.read()
        with open(file_name, 'wb') as f:
            f.write(contents)

        adoc_hist = ADOC_HISTORY_M(file_in=file_in, file_out=file_out, file_out_path=file_name)
        await adoc_hist.upsert()

        all_count = 1
        content = {"msg": "Success", "count": all_count, "filename": file.filename}

        await adoc_excel_file_read(file_name)
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"Error. There was an error uploading the file", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    finally:
        file.file.close()

    return content


async def adoc_excel_file_read(file_in: str):
    print(f"File input {file_in}")
    await ADOC_M.objects.delete(each=True)
    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook(file_in)

    # Define variable to read the active sheet:
    worksheet = wookbook.active

    # Iterate the loop to read the cell values
    # worksheet.max_row
    # worksheet.max_column
    # 18 колонок
    authors = []
    cnt = 0
    for value in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=18, values_only=True):
        print(f"{cnt}")
        cnt = cnt + 1
        folder_root = ''
        folder_link = ''
        folder_short = ''
        folder_name = ''
        rgf = ''
        tgf_hmao = ''
        tgf_ynao = ''
        tgf_kras = ''
        tgf_ekat = ''
        tgf_omsk = ''
        tgf_novo = ''
        tgf_more = ''
        tgf_tmn = ''
        tgf = ''
        report_name = ''
        author_name = ''
        year_str = ''

        territory_name = ''

        # Путь полный
        folder_root = str_get_full_path_with_format(value[0])
        folder_link = folder_root  # Гиперссылка
        folder_short = str_get_folder(folder_root)
        if value[4]:
            rgf = str(value[4])
        if value[5]:
            tgf_hmao = str(value[5])
        if value[6]:
            tgf_ynao = str(value[6])
        if value[7]:
            tgf_kras = str(value[7])
        if value[8]:
            tgf_ekat = str(value[8])
        if value[9]:
            tgf_omsk = str(value[9])
        if value[10]:
            tgf_novo = str(value[10])
        if value[11]:
            tgf_more = str(value[11])
        if value[12]:
            tgf_tmn = str(value[12])

        if len(tgf_tmn):
            tgf = 'ТюмТГФ'
        if len(tgf_more):
            tgf = 'МорскойТГФ'
        if len(tgf_novo):
            tgf = 'НовосибТГФ'
        if len(tgf_omsk):
            tgf = 'ОмскТГФ'
        if len(tgf_ekat):
            tgf = 'ЕкатерТГФ'
        if len(tgf_kras):
            tgf = 'КраснТГФ'
        if len(tgf_ynao):
            tgf = 'ЯНТГФ'
        if len(tgf_hmao):
            tgf = 'ХМТГФ'
        if len(rgf):
            tgf = 'РГФ'

        print(tgf)

        if value[14]:
            report_name = str(value[14]).strip().replace("                              ", "").replace("_x001E_", "")

        if value[15]:
            author_name = str(value[15]).strip()
            author_tmp = author_name.rstrip().replace("и др.", "").rstrip() + ','
            authors.append(author_tmp)

        if value[16]:
            year_str = str(value[16]).strip()
            print(year_str)

        if value[17]:
            territory_name = str(value[17]).strip()
            print(territory_name)

        # adoc = ADOC_M(
        #     folder_root=folder_root,
        #     folder_link=folder_link,
        #     folder_short=folder_short,
        #     folder_name=folder_name,
        #     rgf=rgf,
        #     tgf_hmao=tgf_hmao,
        #     tgf_ynao=tgf_ynao,
        #     tgf_kras=tgf_kras,
        #     tgf_ekat=tgf_ekat,
        #     tgf_omsk=tgf_omsk,
        #     tgf_novo=tgf_novo,
        #     tgf_more=tgf_more,
        #     tgf_tmn=tgf_tmn,
        #     tgf=tgf,
        #     report_name=report_name,
        #     author_name=author_name,
        #     year_str=year_str,
        #     year_int=0,
        #     territory_name=territory_name,
        #     comments=''
        # )
        # await adoc.upsert()

        await ADOC_M(
            folder_root=folder_root,
            folder_link=folder_link,
            folder_short=folder_short,
            folder_name=folder_name,
            rgf=rgf,
            tgf_hmao=tgf_hmao,
            tgf_ynao=tgf_ynao,
            tgf_kras=tgf_kras,
            tgf_ekat=tgf_ekat,
            tgf_omsk=tgf_omsk,
            tgf_novo=tgf_novo,
            tgf_more=tgf_more,
            tgf_tmn=tgf_tmn,
            tgf=tgf,
            report_name=report_name,
            author_name=author_name,
            year_str=year_str,
            year_int=0,
            territory_name=territory_name,
            comments=''
        ).save()

        # str_tmp1 = ''
    authors_str = ",".join(authors)
    authors2 = authors_str.split(",")
    authors = sorted(set(authors2))

    # print(value[2])
    print(f"новая строка {authors}")

    # for i in range(1, 5):
    # for col in worksheet.iter_cols(0, 18):
    # print(col[i].value )
    # print(col[1].value)
    #         # end = "\t\t"
    #     print('')

    # print(worksheet.max_column)
    # print(worksheet.max_row)


def str_get_full_path_with_format(str_in: str):
    if str_in.endswith('\\'):
        str_tmp = str_in.removesuffix('\\')
        return str_tmp
    else:
        return str_in


def str_get_folder(str_in: str):
    str_arr = str_in.rsplit('\\', 1)
    if len(str_arr):
        str_tmp = str(str_arr[1])
    else:
        str_tmp = ""
    return str_tmp

#
# async def files_get_by_root_folder(root_folder: str):
#     content = {"msg": f"Unknown error"}
#     # log = set_logger(settings.WELL_FILE_LOG)
#     try:
#         all_ = await ADOC_M.objects.all(ADOC_M.root_folder == root_folder)
#         all_count = len(all_)
#         # log.info(f"count load successfuly: {all_count}")
#         content = {
#             "msg": "Success",
#             "count": all_count,
#             "data": all_
#         }
#         return content
#     except Exception as e:
#         str_err = "Exception occurred " + str(e)
#         content = {"msg": f"reload fail. can't read count from table {ADOC_M.Meta.tablename}", "err": str(e)}
#         print(str_err)
#         # log.info(str_err)
#     return content


# async def files_get_by_query(str_query: str):
#     content = {"msg": f"Unknown error"}
#     # log = set_logger(settings.WELL_FILE_LOG)
#     try:
#         # books = (
#         #     await Book.objects.filter(Book.author.name.icontains("tolkien"))
#         #     .order_by(Book.year.desc())
#         #     .all()
#         # )
#         # надо сохранять поисковый запрос...
#         print(str_query)
#         # order_by(Book.year.desc())
#         all_ = await FILES_M.objects.filter(FILES_M.file_path.icontains(str_query)).all()
#         all_count = len(all_)
#         # log.info(f"count load successfuly: {all_count}")
#         content = {
#             "msg": "Success",
#             "count": all_count,
#             "data": all_
#             }
#         return content
#     except Exception as e:
#         str_err = "Exception occurred " + str(e)
#         content = {"msg": f"reload fail. can't read from table {FILES_M.Meta.tablename}", "err": str(e)}
#         print(str_err)
#         # log.info(str_err)
#     return content
