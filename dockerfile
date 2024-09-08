FROM python:3.9-slim

WORKDIR /app
COPY stop_and_search.py stop_and_search.py

RUN pip install -r requirements.txt

CMD ["python", "stop_and_search.py"]