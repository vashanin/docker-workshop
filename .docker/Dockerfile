FROM python:3.10

WORKDIR /app

COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .. /app

ENV PYTHONPATH=.:src

ENTRYPOINT uvicorn app:app --reload --host 0.0.0.0 --port 8402