FROM python:3.7-slim

RUN pip install pipenv
WORKDIR /home/app
COPY . .
WORKDIR /home/app/forwarder
RUN pipenv update
ENV PYTHONPATH=/home/app
ENV DOCKER_MODE=true
EXPOSE 8000
CMD ["pipenv", "run", "python", "main.py"]
