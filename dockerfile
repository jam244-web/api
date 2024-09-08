FROM python:3.9-slim

WORKDIR /app
COPY 

RUN pip install -r requirements.txt

CMD ["python", "stop_and_search.py"]