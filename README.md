# POTATO Project

## Overview
POTATO (the Panel-based Open Term-level Aggregate Twitter Observatory) is a prototype web application designed to analyze tweets related to specific terms. This project utilizes Docker, Elasticsearch, Streamlit, and Python to provide users with insightful metrics about tweets on topics of interest.

## Features
- **Data Ingestion**: Efficiently ingest Twitter data from TSV files into Elasticsearch.
- **API Querying**: Expose an API to query tweets based on search terms.
- **Aggregate Metrics**: Provide metrics such as:
  - Daily tweet counts
  - Unique user counts
  - Average likes per tweet
  - Tweet geolocation
  - Tweet timing
  - Most active users

## Technologies Used
- **Python**: Programming language for backend logic.
- **Flask**: Web framework to build the API.
- **Elasticsearch**: NoSQL database to store and query tweet data.
- **Docker**: Containerization for consistent development and deployment.
- **Streamlit**: Optional for creating interactive dashboards.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
- Basic knowledge of using the command line.

## Setup Instructions

### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Anshulverma-prg/potatotaska
cd potato_project/
```
Build and Run the Docker Containers
Command-  docker-compose up --build

## Query the API
curl "http://localhost:5000/query?term=music"

