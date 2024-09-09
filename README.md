# FastAPI App with Celery, RabbitMQ, and Flower UI

## Introduction

This project demonstrates a simple integration of FastAPI, Celery, RabbitMQ, and Flower. The purpose is to showcase how these tools work together to build a backend architecture that can handle asynchronous task processing.

## Project Structure

```
simple_app/
├── app/
│   ├── main.py
│   ├── tasks.py
│   └── __init__.py
├── docker-compose.yml
└── Dockerfile
```

## Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)**: A modern, fast web framework for building APIs with Python 3.6+.
- **[Celery](https://docs.celeryq.dev/en/stable/)**: An asynchronous task queue/job queue based on distributed message passing.
- **[RabbitMQ](https://www.rabbitmq.com/documentation.html)**: A message broker that allows communication between distributed systems.
- **[Flower](https://flower.readthedocs.io/en/latest/)**: A real-time web-based monitoring tool for Celery.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/akileshjayakumar/simple-app.git
   cd simple-app
   ```

2. **Build and start the containers**:
   ```bash
   docker-compose up --build
   ```

## Usage

1. **Access the FastAPI app**:
   - Open your browser and navigate to `http://localhost:8000/docs` to see the FastAPI interactive API documentation.

2. **Submit a task**:
   - Use the `/add/{a}/{b}` endpoint to submit a task.
   - Example: `POST http://localhost:8000/add/3/4`

3. **Check task status**:
   - Use the `/result/{task_id}` endpoint to check the status and result of a submitted task.
   - Example: `GET http://localhost:8000/result/{task_id}`

4. **Access the Flower UI**:
   - Open your browser and navigate to `http://localhost:5555` to see the Flower UI.


## Architecture Diagram

![Architecture Diagram](diagram.png)
