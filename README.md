# Streamlit-and-Docker-basics

## Description
This project demonstrates the basics of using Streamlit with Docker. Streamlit is an open-source app framework for Machine Learning and Data Science teams. Docker is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.

## Installation

### Prerequisites
- Python 3.7 or higher
- Docker
- Streamlit
- Pandas (if used)
- NumPy (if used)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/CharlesDc9/Streamlit-and-Docker-basics.git
    cd Streamlit-and-Docker-basics
    ```


## Usage

### Running Streamlit App Locally
1. Navigate to the project directory:
    ```sh
    cd Streamlit-and-Docker-basics
    ```

2. Run the Streamlit Hello:
    ```sh
    streamlit run Hello.py
    ```

### Running Streamlit App with Docker
1. Build the Docker image:
    ```sh
    docker build -t streamlit-app .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8501:8501 streamlit-app
    ```

3. Open your browser and go to `http://localhost:8501` to see the app.

4. If need be you can find the docker image here `https://hub.docker.com/repository/docker/charlesdc9/final_project_tooling/general`
