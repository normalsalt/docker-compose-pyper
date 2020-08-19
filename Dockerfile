FROM python:3.8.5-slim
RUN apt-get update && apt-get install -y --no-install-recommends r-base-core && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ADD src /code/src
WORKDIR /code/src
CMD ["gunicorn", "-b", "0.0.0.0:8000", "sample:api", "--reload"]
