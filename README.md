
## Descripción

En Los Ángeles existe un sistema compartido de bicicletas que brinda datos anónimos acerca
del uso del servicio. La tabla que se proporciona contiene el histórico de viajes que se han
realizado desde 2016.
A continuación se presentan las columnas
que contiene la tabla:

- trip_id: identificador único para el viaje
- duration: duración del viaje en minutos
- start_time: dia/hora donde en viaje inicia 
- end_time: dia/hora donde el viaje termina 
- start_station: la estación donde el viaje inició
- start_lat: la latitud de la estación donde el viaje se originó
- start_lon: la longitud de la estación donde el viaje se originó
- end_station: la estación donde el viaje terminó
- end_lat: la latitud de la estación donde terminó el viaje
- end_lon: la longitud de la estación donde terminó el viaje
- bike_id: un entero único que identifica la bicicleta
- plan_duration: número de días que el usuario tendrá el paso. 0 significa un viaje único
(Walk-up plan)
- trip_route_category: “Round trip” son viajes que empiezan y terminan en la misma
estación
- passholder_type: El nombre del plan de passholder


## Planificación
Para desarrollar el proyecto se siguio la metodolofía Scrum, se uso [Notion](https://tungsten-basilisk-0b4.notion.site/03ad9781d53640a3926ec46b02ad98d8?v=14b582a25f3340909390b11ef31035a9) para la planeacion y seguimiento de actividades.

## Análisis Exploratorio

En el analísis exploratorio se describe el uso del servicio a través del tiempo, cuales son los días y horas con mayor demanda, así como en que estaciones suceden la mayoría de los viajes. También se aborda el tema de el uso de los diferentes tipos de pases y su relación con el uso del servicio.

Notebook del [Analisis Exploratorio](https://github.com/alexrods/Bicycles-LA-Analysis/blob/main/ds_test_EDA.ipynb)

## Modelo Predictivo

En esta sección se desarrolo un modelo de clasificación con el objetivo de predecir el tipo de pase *Passholder_type* a partir del comportamiento del usuario. El modelo realiza clasificaciones con una precición del 70%.

Notebook del [Analísis Predictivo](https://github.com/alexrods/Bicycles-LA-Analysis/blob/main/ds_test_Analytics.ipynb)

## Puesta en Producción 

Para el despliegue del modelo predictivo se uso la siguiente arquitectura, se dividió el flujo de trabajo en las secciones de desarrollo y despliegue. 
Nota  : Se hace la propuesta de diferentes servicios en la nube que pueden albergar los datos y la aplicación y ésta pueda ser consumida como una API.
Nota 2: Por el momento el modelo solo se puede consumir de manera local, aún no hay despligue en la nube.
Nota 3: Al momento de correr el modelo no es capaz de realizar predicciones, hay errores por solucionar y éste funcione correctamente.

![production_diagram](https://user-images.githubusercontent.com/66699401/181838639-bcd9fd49-297b-4630-a85f-f1a91e43b2cc.png)

## Instalación

- Crear ambiente virtual
  
      python -m venv venv
  
 - Activar ambiente virtual
        
        # Para linux
        source venv/bin/activate
        
        # Para Windows
        .\venv\Scripts\activate
  
- Clonar repositorio 

      git clone https://github.com/alexrods/Bicycles-LA-Analysis.git
      
- Instalar librerías

      pip install -r api/requirements.txt
      
- Run API

      uvicorn api.main:app

El modelo recibe peticiones a través de SwaggerUI. 
Corre en el puerto:

      http://127.0.0.1:8000

![api-bikes](https://user-images.githubusercontent.com/66699401/181842633-bcae11db-e9c5-4781-bd34-a59ac73936b8.png)




## Empaquetado en Docker

Nota: Al momento de correr el comando `run` arroja errores, hace falta corregir estos errores para que la imagen funcione correctamente.

      #Run in console
      DOCKER_BUILDKIT=1 docker build . -t model-api:v1.0
-

      # Run in console
      docker run -p 8000:8000 model-api:v1.0





