# uvicorn main:app --reload
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src import cfg

from src.routers import api_router
from src.database import database, metadata, engine

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.state.database = database


# Root API
@app.get("/", status_code=200,
         name='Get Info',
         tags=['Главная'],
         description='Получает информацию о сервисе')
def root() -> JSONResponse:
    url_swagger = f"http://{cfg.SERVER_HOST}:{cfg.SERVER_PORT}/docs"

    return JSONResponse(status_code=200,
                        content={
                            "msg": "Success",
                            "Info": "Hello it is ADoc project",
                            "Swagger Documentation": url_swagger})


app.include_router(api_router)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    # metadata.create_all(engine)
    if not database_.is_connected:
        print(f"connecting... {database_.url}")
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


if __name__ == "__main__":
    # set_logger()
    uvicorn.run("main:app", host=cfg.SERVER_HOST, port=int(cfg.SERVER_PORT), reload=True)
