# Change the escape character for Windows
# escape=` (backtick)

# Built off of Python3.8-alpine
FROM python:3.8-alpine

# Send scripts from here to docker
ENV PATH="/scripts:${PATH}"

# Copy local requirements to docker
COPY ./requirements.txt /requirements.txt

# Install them and then clean up
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
