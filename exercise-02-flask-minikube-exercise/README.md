# Flask App Deployment on Minikube

## Objective
Deploy a Python Flask application on a local Kubernetes cluster using Minikube, Docker, kubectl, and YAML configuration.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Project Structure
- `app.py` — Flask web application
- `Dockerfile` — Builds the Docker image
- `flask-deployment.yaml` — Kubernetes Deployment and Service configuration

## Steps to Run

1. Start Minikube:
   `minikube start --driver=docker`

2. Build the Docker image:
   `docker build -t flask-app:latest .`

3. Load the image into Minikube:
   `minikube image load flask-app:latest`

4. Deploy the application:
   `kubectl apply -f flask-deployment.yaml`

5. Verify the Deployment:
   `kubectl get deployments`

6. Check the Pods and Services:
   `kubectl get pods`
   `kubectl get services`

7. Access the application:
   `minikube service flask-app-service --url`

## Expected Output

Hello from Flask on Kubernetes!

## Learning Outcomes
- Created and containerized a Flask application.
- Deployed an application using Kubernetes.
- Configured a Kubernetes Service.
- Verified application status and logs.
