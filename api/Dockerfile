FROM python:3.9.16-slim-buster

COPY ./requirements.txt /api/

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . /api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]