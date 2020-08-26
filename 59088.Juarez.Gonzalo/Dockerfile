FROM python:3
WORKDIR /app/src
RUN git clone https://github.com/juarez-gonza/59088.Juarez.Gonzalo.git && \
./59088.Juarez.Gonzalo/init_script
ENTRYPOINT [ "/bin/bash", "-c", "./59088.Juarez.Gonzalo/super_mega_script_que_corre_coverage_en_todos_los_tests.sh && coverage report"]

