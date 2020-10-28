FROM python:3

RUN git clone https://github.com/Nahuel-Silva/Ahorcado.git

RUN pip install parameterized

WORKDIR /Ahorcado

CMD python3 -m unittest && python3 main.py
