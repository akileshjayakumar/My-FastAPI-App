from celery import Celery

celery_app = Celery('tasks', broker='amqp://rabbitmq:5672//')


@celery_app.task
def add(a, b):
    return a + b


@celery_app.task
def multiply(a, b):
    return a * b
