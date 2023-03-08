from fastapi import UploadFile, File
import os
from src import cfg
from src.adoc.models import ADOC_M, ADOC_HISTORY_M


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
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"Error. There was an error uploading the file", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    finally:
        file.file.close()
    return content

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


