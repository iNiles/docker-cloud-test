FROM ubuntu:xenial
COPY . /src
WORKDIR /src
RUN apt-get update
RUN apt-get install -y python3 \
python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install Flask=0.12
ENTRYPOINT ["python"]
CMD ["UNH698.py"]
