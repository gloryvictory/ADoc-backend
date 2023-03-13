from fastapi import UploadFile, File
import os
from src import cfg
from src.models import ADOC_M, ADOC_HISTORY_M, AUTHOR_M
import openpyxl
import re

from src.utils.mystrings import strip_last, removing_leading_whitespaces, str_cleanup


# import asyncpg


async def author_get_all_count():
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_count = await AUTHOR_M.objects.count()
        # log.info(f"count load successfuly: {all_count}")
        content = {"msg": "Success", "count": all_count}
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {AUTHOR_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content


async def author_get_all():
    content = {"msg": f"Unknown error"}
    try:
        all_ = await AUTHOR_M.objects.all()
        all_count = len(all_)
        content = {
            "msg": "Success",
            "count": all_count,
            "data": all_
        }
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {AUTHOR_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content

