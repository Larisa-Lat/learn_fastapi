from database import new_session, TaskOrm
from schemas import TaskAdd, TaskGet
from sqlalchemy import select


class TaskRepository:
    """layer between an application’s business logic and data storage.
    Its primary purpose is to provide a structured and standardized way to
    access, manage, and manipulate data while abstracting the underlying
    details of data storage technologies."""

    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()  # new task in dict

            task = TaskOrm(**task_dict)  # convert dict to TaskOrm type
            session.add(task)  # adding new task in database
            await session.flush()  # adding primary key and getting it
            await session.commit()  # updating database with new task

            return task.id

    @classmethod
    async def find_all(cls) -> list[TaskGet]:
        async with new_session() as session:
            query = select(TaskOrm) # запрос в базу данных ко всей нашей таблице
            result = await session.execute(query)  # обратись к базе данных через session выполни наш запрос
            task_models = result.scalars().all()  # getting sqlalchimy / обьекты алхимии которые к нам вернутся
            # из result получить все обьекты

            task_schemas = [TaskGet.model_validate(task_model) for task_model in task_models]
            # model_validate проверить что подходит под условия TaskGet,
            # если нет выбросит ошибку если да то конвертирует тип
            return task_schemas
