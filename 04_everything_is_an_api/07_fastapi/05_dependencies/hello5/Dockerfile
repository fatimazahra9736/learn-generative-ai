FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn","05_hello:app","--host","0.0.0.0","--port","8000","--reload" ]