from fastapi import APIRouter

from src.adoc.router import router_adoc
from src.author.router import router_author

api_router = APIRouter(prefix='/api/v1')


@api_router.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}


api_router.include_router(router_adoc, prefix="/adoc", tags=["Документы"])  #
api_router.include_router(router_author, prefix="/author", tags=["Авторы"])  #
