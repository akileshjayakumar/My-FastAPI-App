from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult
from .tasks import celery_app, add, multiply

app = FastAPI()


@app.post("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    """
    Endpoint to add two numbers asynchronously using Celery.
    """
    try:
        task = add.apply_async(args=[a, b])
        return {"task_id": task.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/multiply/{a}/{b}")
def multiply_numbers(a: int, b: int):
    """
    Endpoint to multiply two numbers asynchronously using Celery.
    """
    try:
        task = multiply.apply_async(args=[a, b])
        return {"task_id": task.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/result/{task_id}")
def get_result(task_id: str):
    """
    Endpoint to retrieve the result of a Celery task using its task ID.
    """
    try:
        task_result = AsyncResult(task_id, app=celery_app)
        if task_result.state == 'PENDING':
            return {"status": "PENDING"}
        elif task_result.state == 'SUCCESS':
            return {"status": "SUCCESS", "result": task_result.result}
        elif task_result.state == 'FAILURE':
            return {"status": "FAILURE", "error": str(task_result.result)}
        else:
            return {"status": task_result.state}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
