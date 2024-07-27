README.md

# ELK Stack with Log Generator

## Project Description

This project sets up an ELK (Elasticsearch, Logstash, Kibana) stack using Docker Compose. It includes a custom log generator service that produces log data and feeds it into Logstash, which then indexes the data in Elasticsearch. Kibana is used to visualize the log data stored in Elasticsearch.

### Services Overview

1. **Elasticsearch**:
   - Stores and indexes log data.
   - Runs on port 9200 (HTTP) and 9300 (TCP transport).
   - Configuration ensures it runs as a single-node cluster and disables security features for simplicity.

2. **Logstash**:
   - Processes log data from the log generator and forwards it to Elasticsearch.
   - Runs on port 9600.
   - Configuration file (`logstash.conf`) specifies the input log file and the Elasticsearch output.

3. **Kibana**:
   - Provides a web interface to visualize and explore log data.
   - Runs on port 5601.
   - Connects to Elasticsearch to fetch and display data.

4. **Log Generator**:
   - Generates log data and writes it to a log file.
   - Log data is read by Logstash and sent to Elasticsearch.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Steps

1. **Clone the Repository**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
Build and Start the Services:

sh
Kodu kopyala
docker-compose up --build
Accessing the Services:

Kibana: Open your web browser and go to http://localhost:5601.
Elasticsearch: Can be accessed via http://localhost:9200 (primarily for API calls).
Log Generator and Logstash: These services run in the background and don't require direct access.
Configuration Details
Docker Compose
'''
version: '3.6'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.8.2
    container_name: elasticsearch
    restart: always
    volumes:
      - elastic_data:/usr/share/elasticsearch/data
    environment:
      discovery.type: single-node
      xpack.security.enabled: "false"
      ES_JAVA_OPTS: "-Xmx256m -Xms256m"
      network.host: "0.0.0.0"
      http.port: "9200"
    ports:
      - '9200:9200'
      - '9300:9300'
    networks:
      - elk
    healthcheck:
      test: ["CMD-SHELL", "curl -fsSL http://localhost:9200/_cluster/health || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3

  logstash:
    image: docker.elastic.co/logstash/logstash:8.8.2
    container_name: logstash
    restart: always
    volumes:
      - ./logstash/config/logstash.conf:/usr/share/logstash/config/logstash.conf
      - ./temp:/usr/share/logstash/temp
    command: logstash -f /usr/share/logstash/config/logstash.conf
    depends_on:
      elasticsearch:
        condition: service_healthy
    ports:
      - '9600:9600'
    environment:
      LS_JAVA_OPTS: "-Xmx256m -Xms256m"
    networks:
      - elk
    healthcheck:
      test: ["CMD-SHELL", "curl -fsSL http://localhost:9600 || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3

  kibana:
    image: docker.elastic.co/kibana/kibana:8.8.2
    container_name: kibana
    restart: always
    ports:
      - '5601:5601'
    environment:
      ELASTICSEARCH_HOSTS: "http://elasticsearch:9200"
    depends_on:
      elasticsearch:
        condition: service_healthy
    networks:
      - elk

  log-generator:
    build: .
    container_name: log-generator
    restart: always
    environment:
      LOG_FILE_PATH: /usr/share/logstash/temp/inlog.log
    volumes:
      - ./temp:/usr/share/logstash/temp
    depends_on:
      elasticsearch:
        condition: service_healthy
      logstash:
        condition: service_healthy
    networks:
      - elk

volumes:
  elastic_data: {}

networks:
  elk:
Logstash Configuration
conf
Kodu kopyala
input {
    file {
        path => "/usr/share/logstash/temp/inlog.log"
        start_position => "beginning"
        sincedb_path => "/dev/null"
    }
}

output {
    elasticsearch {
        hosts => ["http://elasticsearch:9200"]
        index => "logstash-index-%{+YYYY.MM.dd}"
    }
    stdout { codec => rubydebug }
}
'''
Log Generator Python Script
python
Kodu kopyala
import time
import random
import os

log_file_path = os.getenv("LOG_FILE_PATH", "/usr/share/logstash/temp/inlog.log")

log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = [
    "User logged in",
    "User logged out",
    "File not found",
    "Error while processing request",
    "Data saved successfully",
    "Connection lost",
    "Reconnected to the server"
]

def generate_log_message():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_level = random.choice(log_levels)
    message = random.choice(messages)
    log_message = f"{timestamp} - {log_level} - {message}\n"
    return log_message

def write_log_to_file(log_message):
    with open(log_file_path, "a") as log_file:
        log_file.write(log_message)

if __name__ == "__main__":
    while True:
        log_message = generate_log_message()
        print(log_message.strip())  # Optional: print log message to console
        write_log_to_file(log_message)
        time.sleep(5)  # Wait for 5 seconds before generating the next log message
