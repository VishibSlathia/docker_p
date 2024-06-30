FROM python:3.10

WORKDIR /app

RUN pip install websockets

COPY responder.py .

CMD ["python", "responder.py"]