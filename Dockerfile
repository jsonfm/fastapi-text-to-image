FROM python:3.11-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /code
WORKDIR $APP_HOME


COPY requirements.txt .

RUN apt update
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
