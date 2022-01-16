FROM python:3.10.1

WORKDIR /app

COPY utils.py .
COPY download.py .
COPY etl.py .
COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
ENTRYPOINT python main.py
