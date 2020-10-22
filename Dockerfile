FROM alpine:3.12

RUN apk add --no-cache python3
RUN apk add --update py-pip
RUN pip3 install --upgrade pip setuptools

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/app.py"]