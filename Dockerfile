FROM python:3.9-slim

RUN mkdir /app
RUN mkdir /app/instance && chmod 777 /app/instance
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN useradd app
USER app

EXPOSE 5000

CMD ["python", "main.py"]
