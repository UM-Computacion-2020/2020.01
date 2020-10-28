FROM python:3

RUN git clone https://github.com/brunobonil/Proyecto-Ahorcado.git

RUN pip3 install parameterized

WORKDIR /Proyecto-Ahorcado

CMD python3.8 test_partida.py && python3.8 test_ahorcado.py -b
