# PypeR API

## Python version

- python:3.8.5-slim

Update `Dockerfile`.

## R version

```
docker-compose run --rm python R --version
```

## Python Package version

- PypeR==1.1.2

Update `requirements.txt`.

# up

```
docker-compose up -d
```

Open `http://localhost:8000/faithful` in your browser; you'll see this output:

```
try({duration.freq})
duration.cut
[1.5,2) [2,2.5) [2.5,3) [3,3.5) [3.5,4) [4,4.5) [4.5,5) [5,5.5)
     51      41       5       7      30      73      61       4
```

# test

```
docker-compose run --rm python python -m unittest
```

# Falcon Framework

https://falconframework.org/

## Falcon version

- falcon>=2.0.0,<3.0.0
- gunicorn>=20.0.4,<21.0.0

Update `requirements.txt`.

## documentation

https://falcon.readthedocs.io/en/stable/

# build

```
docker-compose up -d --build
```
