# Frontend Modbus Smartlogger

Plataforma Monitorización y almacenamiento de variables electricas importadas por los diferentes equipos de una planta fotovoltica

## 0. Servicios

| ID | Contenedor |     Descripción      |           Puerto            |               Url                |
|:--:|:----------:|:--------------------:|:---------------------------:|:--------------------------------:|
| 1  |  Frontend   | Web de visualizacion   |   80          | [front](http://localhost:80) |
| 2  |  Postgres   | BBDD                   |   5432        | -                                |
| 3  |  Restarter  | Crontab                |   -           |                -                 |
| 4  |  Consultas  | Consultar Modbus       |   -           |                -                 |


## 1. Equipos a Monitorizar

| ID | Equipo |  Esclavo |
|:--:|:----------:|:--------------------:|
| 1  |  Smartlogger     | 100   |
| 2  |  Inversor        | 65    |
| 3  |  AARR            | 5     |
| 4  |  EMI             | 7     |