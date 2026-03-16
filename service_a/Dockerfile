FROM python:3.13

WORKDIR /app

COPY ./service_a/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./service_a ./service_a
COPY ./shard ./shard

CMD ["python", "-m", "service_a.main" ]

