FROM python:3

RUN git clone https://github.com/Marianagiacconi/tp-06.git

COPY src /

RUN  pip install parameterized

WORKDIR /

CMD ["python3","-m","unittest"]