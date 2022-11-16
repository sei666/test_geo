FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV ENV_FILE_LOCATION=./.env

CMD ["python3", "-u", "run.py"]