# from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT
import uuid
import ormar
from datetime import datetime
# import ormar_postgres_full_text


from src.database import database, metadata


# metadata = MetaData()

class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class BaseClass(ormar.Model):
    class Meta(MainMeta):
        abstract = True
        # tablename = "Fields"
        pass

    # id: uuid.UUID = ormar.UUID(default=uuid.uuid4, primary_key=True)
    id: int = ormar.Integer(primary_key=True)
    lastupdate: datetime = ormar.DateTime(default=datetime.now)


class ADOC_M(BaseClass):
    class Meta(MainMeta):
        tablename = "adoc"
        pass

    # id: uuid.UUID = ormar.UUID(default=uuid.uuid4, primary_key=True, uuid_format='string')
    folder_root: str = ormar.Text(index=True)
    folder_link: str = ormar.Text(index=True)
    folder_short: str = ormar.Text(index=True)
    folder_name: str = ormar.Text(index=True)
    rgf: str = ormar.String(index=True, max_length=255)
    tgf_hmao: str = ormar.String(index=True, max_length=255)
    tgf_ynao: str = ormar.String(index=True, max_length=255)
    tgf_kras: str = ormar.String(index=True, max_length=255)
    tgf_ekat: str = ormar.String(index=True, max_length=255)
    tgf_omsk: str = ormar.String(index=True, max_length=255)
    tgf_novo: str = ormar.String(index=True, max_length=255)
    tgf_more: str = ormar.String(index=True, max_length=255)
    tgf_tmn: str = ormar.String(index=True, max_length=255)
    tgf: str = ormar.String(index=True, max_length=255)
    report_name: str = ormar.Text()
    author_name: str = ormar.Text(index=True)
    year_str: str = ormar.String(index=True, max_length=255)
    year_int: str = ormar.Integer(index=True)
    territory_name: str = ormar.Text(index=True)
    comments: str = ormar.Text(index=True)
    # file_path_fts: str = ormar_postgres_full_text.TSVector()


class ADOC_HISTORY_M(BaseClass):
    class Meta(MainMeta):
        tablename = "adoc_history"
        pass

    file_in: str = ormar.String(max_length=255)
    file_out: str = ormar.String(max_length=255)
    file_out_path: str = ormar.Text()
    # id: int = ormar.Integer(primary_key=True)
    # lastupdate: datetime = ormar.DateTime(default=datetime.now)


class AUTHOR_M(BaseClass):
    class Meta(MainMeta):
        tablename = "author"
        pass

    author_name: str = ormar.String(index=True, max_length=255)
    # id: int = ormar.Integer(primary_key=True)
    # lastupdate: datetime = ormar.DateTime(default=datetime.now)