# DevOps Assignment: Docker, Kubernetes, and Pulumi

This project combines Docker, Kubernetes, and Pulumi to create a containerized NGINX web server.

## Technologies Used

- Docker
- Kubernetes (K8s)
- Pulumi

## Project Description

The goal of this project is to demonstrate the integration of Docker, Kubernetes, and Pulumi to deploy a containerized NGINX web server. The project includes the following components:

- A Dockerfile that defines the NGINX container image based on Alpine Linux.
- A Pulumi program written in Python (or a language of your preference) that orchestrates the deployment on a Kubernetes cluster.
- A simple HTML webpage served by NGINX.

## Getting Started

Follow these steps to set up and deploy the project:

1. **Kubernetes Cluster**: Install a Kubernetes cluster on your computer. Minikube is a good option for local development.

2. **Dockerfile**: Create a simple Dockerfile that is based on Alpine Linux and includes NGINX.

3. **Build the Docker Image**: Build the Docker image locally.

4. **Pulumi Deployment**: Create a Pulumi deployment program in your preferred language. The deployment should include:
   - A Kubernetes Deployment for NGINX with 4 pods.
   - Resource requests and limits, and volume mounts for persistent storage.
   - A Kubernetes Service to expose NGINX ports for HTTP and HTTPS.

5. **Pulumi Deploy**: Use Pulumi to deploy your stack to the Kubernetes cluster.

6. **Static Webpage**: Create a simple HTML webpage to be served by NGINX.

7. **Testing**: Verify that the NGINX server is up and running. You can access the webpage using port forwarding.






