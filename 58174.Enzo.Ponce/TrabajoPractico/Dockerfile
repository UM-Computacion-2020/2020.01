FROM python:3

RUN git clone https://github.com/EnzoPonce/Docker.git

RUN pip3 install parameterized

WORKDIR /Docker

CMD ["python3", "-m", "unittest"]
