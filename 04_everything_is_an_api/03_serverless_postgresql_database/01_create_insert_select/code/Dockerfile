FROM jupyter/base-notebook:latest

WORKDIR /app

COPY . .

EXPOSE 8888

CMD [ "jupyter","notebook","--port","8888","--no-browser","--allow-root"]

