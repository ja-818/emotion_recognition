FROM python:3.9.16-slim-buster as base

COPY ./requirements.txt /model/

RUN pip install --no-cache-dir --upgrade -r /model/requirements.txt

# COPY . /model

# # CMD ["python", "/model/middleware.py"]
# FROM base as build
# ENTRYPOINT ["python", "/model/ml_service.py"]

ENV PYTHONPATH=$PYTHONPATH:/src/
ADD ./ /src/
WORKDIR /src

FROM base as build
ENTRYPOINT ["python3", "/src/main.py"]