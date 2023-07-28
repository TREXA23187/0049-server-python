FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8088

# Run app.py when the container launches
#CMD ["python", "run.py"]
ENTRYPOINT ["python","-u", "run.py"]
