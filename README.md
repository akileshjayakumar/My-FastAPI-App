# FastAPI App with Celery, RabbitMQ, and Flower UI

## Introduction

This project demonstrates the integration of FastAPI, Celery, RabbitMQ, and Flower. It highlights how these tools can work together to build a backend architecture capable of handling asynchronous task processing.

## Project Structure

```
app/
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
- **[RabbitMQ](https://www.rabbitmq.com/documentation.html)**: A message broker that facilitates communication between distributed systems.
- **[Flower](https://flower.readthedocs.io/en/latest/)**: A real-time web-based monitoring tool for Celery tasks.

## Setup

### 1. Clone the repository
   - First, clone the repository from GitHub:
     ```bash
     git clone https://github.com/akileshjayakumar/my-fastapi-app
     ```
   - Navigate into the project directory:
     ```bash
     cd my-fastapi-app
     ```

### 2. Build and start the containers
   - Run the following command to build and start the Docker containers:
     ```bash
     docker compose up --build
     ```

## Usage

### 1. Access the FastAPI app
   - Open your browser and navigate to `http://localhost:8000/docs` to explore the interactive FastAPI API documentation.

### 2. Submit a task
   - Use the `/add/{a}/{b}` endpoint to submit an asynchronous task.
   - Example: 
     ```http
     POST http://localhost:8000/add/3/4
     ```

### 3. Check task status
   - Use the `/result/{task_id}` endpoint to check the status and result of a submitted task.
   - Example: 
     ```http
     GET http://localhost:8000/result/{task_id}
     ```

### 4. Access the Flower UI
   - Open your browser and navigate to `http://localhost:5555` to monitor Celery tasks via the Flower UI.

## Architecture Diagram

![Architecture Diagram](diagram.png)
