# from typing import AsyncGenerator
# from sqlalchemy import MetaData
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# alembic init alembic
# alembic revision --autogenerate -m "Commit message"
# alembic revision -m "init"
# alembic upgrade head

from src import cfg
import databases
import sqlalchemy

# sys.path.append("..")

engine = sqlalchemy.create_engine(cfg.DB_DSN)
database = databases.Database(cfg.DB_DSN)
metadata = sqlalchemy.MetaData(schema=cfg.DB_SCHEMA) # чтобы складывать в одну схему

# 3. Database creation and tables creation
# metadata.create_all(engine)




# from cfg import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Base = declarative_base()
# # connect_args={'options': '-csearch_path={}'.format('public')}
# engine = create_async_engine(cfg.DATABASE_URL)
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session

