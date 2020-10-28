FROM python:3

RUN git clone https://github.com/militomba/TrabajoPracticoAhorcado.git

RUN pip3 install parameterized

WORKDIR /TrabajoPracticoAhorcado

CMD python3 -m unittest && python3 main.py
