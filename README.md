# Simple FastAPI, Celery, RabbitMQ, and Flower App

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

## Components

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.6+.
- **Celery**: An asynchronous task queue/job queue based on distributed message passing.
- **RabbitMQ**: A message broker that allows communication between distributed systems.
- **Flower**: A real-time web-based monitoring tool for Celery.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/simple-app.git
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

## File Descriptions

- `app/main.py`: Contains the FastAPI application and endpoints.
- `app/tasks.py`: Defines the Celery tasks.
- `Dockerfile`: Docker configuration for building the FastAPI app image.
- `docker-compose.yml`: Docker Compose configuration for setting up FastAPI, Celery, RabbitMQ, and Flower.

## Architecture

The architecture involves the following components working together:

- **FastAPI** handles incoming requests and triggers tasks.
- **Celery** processes tasks asynchronously using RabbitMQ as a message broker.
- **Flower** monitors the status of tasks and workers.

## Diagram

![Architecture Diagram](diagram.png)

## Contributing

Your contributions are welcome! If you have ideas for improvements or new features:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Submit a pull request.

## Contact Information

For more information, please reach out to me at:

- **Email**: [jayakuma006@mymail.sim.edu.sg](mailto:jayakuma006@mymail.sim.edu.sg)
- **LinkedIn**: [Akilesh Jayakumar on LinkedIn](https://www.linkedin.com/in/akileshjayakumar/)
- **GitHub**: [Akilesh Jayakumar on GitHub](https://github.com/akileshjayakumar)