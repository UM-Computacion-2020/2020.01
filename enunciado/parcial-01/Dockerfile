FROM python:3

#RUN git clone https://github.com/

COPY src parcial

RUN pip install parameterized

WORKDIR /parcial

CMD ["python3","-m" ,"unittest"]
