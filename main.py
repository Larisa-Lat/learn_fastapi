from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import delete_table, create_table

from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Чтобы автоматически очистить таблицу и создать новую"""
    await delete_table()
    print("База очищена")
    await create_table()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



