FROM python:3.10-alpine
EXPOSE 5000
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN apk add --no-cache curl

CMD ["python", "main.py"]