FROM python:3

RUN git clone https://github.com/aguevabb/my_docker.git

RUN pip3 install parameterized

WORKDIR /my_docker

CMD ["python3", "-m", "unittest"]