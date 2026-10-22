### Project Setup and Docker Guide

### 1. Environment Setup

Create and activate the Conda environment, then install dependencies: 

bash

conda create -n test python=3.11 -y 

Use code with caution.

bash

conda activate test 

Use code with caution.

bash

pip install -r requirements.txt 

Use code with caution.

### 2. Docker Test

Test your Docker installation with the hello-world image: 

bash

docker pull hello-world 

Use code with caution.

bash

docker run hello-world 

Use code with caution.

### Useful Docker Management Commands:

bash

docker ps                                   # See a list of all running containers
docker ps -a                                # See a list of all containers, even the ones not running
docker rm                             # Remove the specified container from this machine
docker rm $(docker ps -a -q)                # Remove all containers from this machine
docker images -a                            # Show all images on this machine
docker rmi                       # Remove the specified image from this machine
docker rmi $(docker images -q)              # Remove all images from this machine

Use code with caution.

### 3. Docker Custom Image

Build and run your custom application locally: 

bash

docker build -t subodhkryadav/mycalapp:latest . 

Use code with caution.

Run in foreground (interactive mode): 

bash

docker run -p 8080:8080 subodhkryadav/mycalapp:latest 

Use code with caution.

Run in background (detached mode): 

bash

docker run -d -p 8080:8080 subodhkryadav/mycalapp:latest 

Use code with caution.

### 4. Push to Docker Hub

Log in and push your image to the Docker Hub repository: 

bash

docker login

Use code with caution.

bash

docker push subodhkryadav/mycalapp:latest

Use code with caution.