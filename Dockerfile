FROM python:3.9
ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN mkdir app
WORKDIR /app
COPY . /app

CMD ["python", "main.py"]
