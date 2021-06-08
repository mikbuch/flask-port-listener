FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install Flask

ENV http_proxy=http:...
ENV https_proxy=http:...
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

WORKDIR /app

COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
