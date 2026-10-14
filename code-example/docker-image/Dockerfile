FROM python:3.11-slim-bookworm

ENV AUTH_KEY=
ENV ENABLE_KAFKA_STREAMING=
ENV KAFKA_BOOTSTRAP_SERVER=
ENV KAFKA_TOPIC=
ENV KAFKA_USERNAME=
ENV KAFKA_PASSWORD=
ENV KAFKA_SECURITY_PROTOCOL=

RUN apt-get update -q \
    && apt-get install --no-install-recommends -qy nginx openssl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /api

COPY requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/cert.key -out /etc/nginx/cert.crt -subj "/CN=127.0.0.1"

RUN rm -f /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/

EXPOSE 443

COPY app.py preprocess.py ./
COPY text_classification_cnn_model.h5 .
COPY tokenizer.pickle .
COPY label_encoder.pickle .

CMD service nginx start && python3 app.py
