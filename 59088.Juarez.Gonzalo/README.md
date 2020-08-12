El Dockerfile en la base de la carpeta es el que se usó para el repositorio en docker hub del cual el
resto de las imágenes dependen. Clona el repositorio de git e instala dependencias (como parameterized).
La imagen base se crea una sola vez y todas las otras imágenes (de los trabajos) la comparten como capa inferior.

link del repositorio con el código:
    https://github.com/juarez-gonza/59088.Juarez.Gonzalo.git

# COMANDOS
    docker-compose up --> para levantar imagenes y containers de todos los trabajos al mismo tiempo.
    docker-compose down --> para remover los containers de todos los trabajos al mismo tiempo (no remueve imágenes).
    # usando docker-compose up los trabajos que esperen input por stdin paran al inciar por error EOF
    # (trata de leer stdin pero no hay stdin ligado al container).
    otros comandos:
        docker-compose stop
        docker-compose start
        docker-compose logs [opciones] [nombre_servicio (i.e tp1)] --> display del output del servicio (en este caso, que consiste de
            1 solo container).
        docker-compose exec [nombre_servicio] --> como docker container exec
        
        
    docker run [opciones] [contexto] --> o dirigirse a alguna carpeta con un Dockerfile (o usar -f /path/a/Dockerfile).
    (el contexto puede ser la ubicación actual, en este caso -por ahora- no afecta al funcionamiento).
    # para los trabajos que usan input por stdin pueden usarse los flags -i y -t, o resumido, -it (interactivo y pseudo terminal).