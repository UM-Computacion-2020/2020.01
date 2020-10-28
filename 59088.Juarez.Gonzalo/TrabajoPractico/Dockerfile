FROM python:3
WORKDIR /app
RUN git clone https://github.com/juarez-gonza/computacion_practico_final.git && \
        ./computacion_practico_final/init_script.sh
ENTRYPOINT [ "/bin/bash", "-c", "/app/computacion_practico_final/generar_reporte.sh" ]
