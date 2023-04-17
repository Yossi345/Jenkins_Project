FROM alpine:latest
WORKDIR /app
COPY run.py requirements.txt /app/
RUN apk add --update python3 py3-pip
RUN pip install -r requirements.txt
RUN apk add --no-cache aws-cli
CMD python run.py
