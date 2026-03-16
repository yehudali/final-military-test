FROM python:3.13

WORKDIR /app

COPY KafkaSimulator/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./KafkaSimulator ./KafkaSimulator
# COPY ./shard ./shard

CMD ["python", "-m", "KafkaSimulator.simulator" ]

