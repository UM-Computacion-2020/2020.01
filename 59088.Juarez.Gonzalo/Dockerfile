FROM python:3
WORKDIR /app/src
RUN git clone https://github.com/juarez-gonza/59088.Juarez.Gonzalo.git && \
./59088.Juarez.Gonzalo/init_script && pip3 list && echo $PWD
ENTRYPOINT [ "/bin/bash", "-c", "./super_mega_script_que_corre_coverage_en_todos_los_tests.sh"]

