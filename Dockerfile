FROM python:3.10.1

WORKDIR /app

COPY download.py .
COPY merge.py .
COPY utils.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
ENTRYPOINT python download.py
