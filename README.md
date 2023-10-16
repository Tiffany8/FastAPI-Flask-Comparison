# 🍔 FastAPI vs Flask: Serving Requests Daily 🍟

## About 📚

This repository contains the code accompanying my Medium blog post, "Order Up! FastAPI vs Flask in the Kitchen of RESTful APIs.".

👉 [Read the full blog post on Medium](https://medium.com/@TWilliamsPhD/77f4ec738f82)


## Getting Started 🚀

### Prerequisites 📋

- Python 3.x
- Pipenv or Poetry for package management

### Installation 🔧

1. Clone the repository
    ```bash
    git clone https://github.com/Tiffany8/FastAPI-Flask-Comparison.git
    ```

2. Navigate to project
```bash
cd FastAPI-Flask-Comparison
```

3. Install dependencies
    ```bash
    poetry shell && poetry install
    ```

### Running the Examples 🏃‍♀️

FastAPI:
```bash
uvicorn fastapi_example.main:app --reload --port=8000
```

Flask:
```bash
gunicorn flask_example.main:app --reload --bind 0.0.0.0:8001
```

