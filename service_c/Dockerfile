FROM python:3.13

WORKDIR /app

COPY ./service_b/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./service_c ./service_c
COPY ./shard ./shard

CMD ["python", "-m", "service_c.main" ]

