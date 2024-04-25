from sqlalchemy.ext.asyncio import create_async_engine  # движок баз данных
from sqlalchemy.ext.asyncio import async_sessionmaker  # фабрика созданий сессий
# открытие транзакций для работы с базой данных
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional


engine = create_async_engine(
    url="sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    """Описание таблицы"""
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


async def create_table():
    """function to create table"""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_table():
    """function to delete table"""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)




