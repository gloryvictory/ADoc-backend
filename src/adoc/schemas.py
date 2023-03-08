from datetime import datetime

from pydantic import BaseModel


class ADOC_S(BaseModel):
    id: int
    folder_root: str
    folder_link: str
    folder_short: str
    folder_name: str
    rgf: str
    tgf_hmao: str
    tgf_ynao: str
    tgf_kras: str
    tgf_ekat: str
    tgf_omsk: str
    tgf_novo: str
    tgf_more: str
    tgf_tmn: str
    tgf: str
    report_name: str
    author_name: str
    year_str: str
    territory_name: str
    lastupdate: datetime

    class Config:
        orm_mode = True


class ADOC_HISTORY_S(BaseModel):
    id: int
    file_in: str
    file_out: str
    file_out_path: str
    lastupdate: datetime


    class Config:
        orm_mode = True