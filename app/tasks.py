# tasks.py

from celery import Celery

# Configure Celery with both broker and backend
celery_app = Celery(
    'tasks',
    broker='amqp://rabbitmq:5672//',
    backend='redis://redis:6379/0'  # Using Redis as the result backend
)

# Optional: Celery configuration settings
celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)


@celery_app.task(bind=True)
def add(self, a, b):
    """
    Celery task to add two numbers.
    """
    return a + b


@celery_app.task(bind=True)
def multiply(self, a, b):
    """
    Celery task to multiply two numbers.
    """
    return a * b
