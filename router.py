from fastapi import Depends, APIRouter
from schemas import TaskAdd
from typing import Annotated
from repository import TaskRepository
from schemas import TaskGet, TaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]  # список тегов
)


@router.post(path="") # путь указан в роутере в атрибуте prefix
async def get_task(
        task: Annotated[TaskAdd, Depends()]
) -> TaskId:
    # махинации с базой данных
    # добавление одного таска через паттерн репозитория
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get(path="")  # путь указан в роутере в атрибуте prefix
async def get_tasks() -> list[TaskGet]:
    tasks = await TaskRepository.find_all()  # получим json формат
    return tasks
