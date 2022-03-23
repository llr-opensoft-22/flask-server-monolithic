# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install flask flask_cors flask_swagger_ui supabase_client prometheus_client
COPY . .
CMD [ “python3”, “-m” , “flask”, “run”, “--host=0.0.0.0”]
EXPOSE 8000