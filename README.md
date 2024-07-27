<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][https://github.com/Berko01]
[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/berkindundar/]

<!-- PROJECT LOGO -->
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot](elk.jpeg)

This project sets up an ELK (Elasticsearch, Logstash, Kibana) stack using Docker Compose. It includes a custom log generator service that produces log data and feeds it into Logstash, which then indexes the data in Elasticsearch. Kibana is used to visualize the log data stored in Elasticsearch.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

### Built With

This project leverages the following major frameworks and libraries to set up and manage the ELK stack and the custom log generator:

- **Docker**: Used to containerize the various services (Elasticsearch, Logstash, Kibana, and the log generator). Docker ensures that each service runs in an isolated environment, making the setup process straightforward and consistent across different environments.
- **Docker Compose**: Simplifies the process of managing multi-container Docker applications. With Docker Compose, we can define and run the entire stack using a single YAML file.
- **Elasticsearch**: A highly scalable open-source full-text search and analytics engine. It is used to store, search, and analyze the log data generated by the log generator.
- **Logstash**: An open-source server-side data processing pipeline that ingests data from multiple sources, transforms it, and then sends it to your preferred "stash". In this project, Logstash reads log data from the log generator and sends it to Elasticsearch.
- **Kibana**: An open-source data visualization and exploration tool used for reviewing the log data stored in Elasticsearch. It provides a user-friendly web interface to create visualizations, dashboards, and more.
- **Python**: Used to write the custom log generator script. The script simulates log data generation and writes the logs to a file, which is then read by Logstash.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Steps

1. **Clone the Repository**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   docker-compose up --build
