FROM python:3.8

RUN git clone https://github.com/MatiasTomasRobbio/Ahorcado_Matias_Robbio.git
RUN pip3 install parameterized

WORKDIR /Ahorcado_Matias_Robbio

CMD python3.8 test_partida.py && python3.8 test_ahorcado.py -b && python3.8 ahorcado.py

