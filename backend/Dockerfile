FROM python:3.9

RUN mkdir -p backend/app
COPY app/requirements.txt /backend/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/app/requirements.txt

COPY app /backend/app
EXPOSE 8004

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8004", "--reload"]