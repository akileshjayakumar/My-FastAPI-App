from fastapi import FastAPI, BackgroundTasks
from celery.result import AsyncResult
from .tasks import celery_app, add, multiply

app = FastAPI()


@app.post("/add/{a}/{b}")
def add_numbers(a: int, b: int, background_tasks: BackgroundTasks):
    task = add.apply_async(args=[a, b])
    background_tasks.add_task(check_task_status, task.id)
    return {"task_id": task.id}


@app.post("/multiply/{a}/{b}")
def add_numbers(a: int, b: int, background_tasks: BackgroundTasks):
    task = multiply.apply_async(args=[a, b])
    background_tasks.add_task(check_task_status, task.id)
    return {"task_id": task.id}


@app.get("/result/{task_id}")
def get_result(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.state == 'PENDING':
        return {"status": "PENDING"}
    elif task_result.state == 'SUCCESS':
        return {"status": "SUCCESS", "result": task_result.result}
    else:
        return {"status": task_result.state}


def check_task_status(task_id):
    result = AsyncResult(task_id, app=celery_app)
    if result.state == 'SUCCESS':
        print(f"Task {task_id} completed with result: {result.result}")
    else:
        print(f"Task {task_id} status: {result.state}")
