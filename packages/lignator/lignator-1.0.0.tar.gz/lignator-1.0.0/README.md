# lignator-code

Procesa cargas de datos nuevos en el sistema menso-app


# Setup

Instalar

```sh
pip install poetry
poetry install
```


# Run

Procesar archivo

```sh
lignator process --file data/CR1000X_GenericTable.dat.gz
```


Sólo leer encabezados del formato

```sh
lignator headers --file data/CR1000X_GenericTable.dat.gz
```

`lignator --help` para consultar por todas las opciones
