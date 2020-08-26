se puede correr de 2 maneras.
        docker-compose up
                crea una imagen y corre un container para cada trabajo en particular.
                para limpiar todos los containers e imagenes está el ./script_limpieza.

        o bien armar con "Docker build . " el Dockerfile q está en la misma carpeta q este archivo
                crea solo una imagen q al ser instanciada como container corre todos los tests
                y muestra la cobertura del código.
