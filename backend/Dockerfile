FROM python:3.10.13-slim

RUN mkdir -p backend/app
RUN pip install "poetry==1.6.1"
COPY poetry.lock pyproject.toml /backend/
WORKDIR /backend

RUN poetry install --no-interaction --no-ansi

# COPY app/requirements.txt /backend/app/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /backend/app/requirements.txt

EXPOSE 8004

# CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8004", "--reload"]