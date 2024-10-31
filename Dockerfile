FROM python:3.8-slim

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/

CMD ["python", "./app/main.py"]