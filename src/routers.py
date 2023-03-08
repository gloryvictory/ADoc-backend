from fastapi import APIRouter

from src.adoc.router import router_files

api_router = APIRouter(prefix='/api/v1')


@api_router.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}


api_router.include_router(router_files, prefix="/adoc", tags=["Документы"])  #
