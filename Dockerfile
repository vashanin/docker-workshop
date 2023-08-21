FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH=.:src

ENTRYPOINT uvicorn app:app --reload --port 8402