# Exercise 1 - Hello Pod

## Overview
Deploy and access a sample web application on a local Kubernetes cluster using Minikube and Nginx.

**Business Scenario:** Simulate deploying a Zepto storefront application as a DevOps Engineer using an Nginx container.

## Objectives
- Start a local Kubernetes cluster.
- Create and verify a Pod.
- Expose the application using a NodePort Service.
- Access the application through a browser.

## Technologies Used
- Kubernetes
- Minikube
- kubectl
- Nginx
- Docker

## Prerequisites
- Minikube installed
- kubectl installed
- Docker or another supported Minikube driver

## Implementation

### 1. Start the Cluster
```bash
minikube start
```

### 2. Create a Pod
```bash
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod
```bash
kubectl get pods
```

### 4. Expose the Pod
```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Access the Application
```bash
minikube service hello-k8s
```

The Nginx welcome page should open in the browser.

## Key Concepts
- **Pod:** Smallest deployable unit in Kubernetes.
- **Container:** Runs the Nginx web server.
- **Service:** Provides network access to the application.
- **NodePort:** Exposes a Service through a port on the cluster node.
- **kubectl:** Command-line tool for managing Kubernetes resources.

## Cleanup
```bash
kubectl delete service hello-k8s
kubectl delete pod hello-k8s
minikube stop
```

## Expected Outcome
Successfully deployed an Nginx Pod on Kubernetes and accessed it through a NodePort Service.

## Next Exercise
Deploy an application using a Kubernetes Deployment.

---


# exercise 2 - Flask App Deployment on Minikube

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


# Exercise 3: Scaling Flask App Using Kubernetes ReplicaSets

## Overview
Deploy a Flask-based flash-sale application on Kubernetes and demonstrate scaling and self-healing using ReplicaSets.

## Technologies
- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Application Endpoints
- `/` – Welcome message and serving Pod name.
- `/buy?user=123` – Simulates a flash-sale purchase.
- `/health` – Application health check.

## Implementation
1. Build the Flask application Docker image.
2. Deploy three replicas using a Kubernetes ReplicaSet.
3. Expose the application using a NodePort Service.
4. Scale the ReplicaSet from three to five replicas.
5. Delete a Pod and verify automatic replacement.
6. Inspect Pod distribution using `kubectl get pods -o wide`.

## Key Learnings
- ReplicaSets maintain the desired number of Pods.
- Scaling increases or decreases the number of replicas.
- Kubernetes replaces deleted Pods to maintain the desired replica count.
- Services provide a stable endpoint for accessing application Pods.
- Multiple Pods on one node demonstrate replica scaling, not multi-node availability.

## Expected Outcome
A Flask application running with five healthy replicas on a single-node Minikube cluster, with successful scaling and self-healing verification.

## Evidence
See the `screenshots/` directory for execution results.

## Cleanup
```bash
kubectl delete -f flashsale-replicaset.yaml
```


# Exercise 4: Docker Networking with Multiple Containers

## Objective
Configure a custom Docker bridge network and enable communication between Flask, MySQL, and Redis containers.

## Technologies Used
- Docker
- Python
- Flask
- MySQL
- Redis

## Implementation
1. Created a custom bridge network named `my-bridge-net`.
2. Built the Flask REST API image.
3. Started MySQL, Redis, and Flask containers on the same network.
4. Published the Flask application on port 5001.
5. Tested API endpoints and container connectivity.
6. Inspected the network and connected containers.

## API Endpoints
- `/about` — Returns application information.
- `/health` — Returns application health status.

## Key Learnings
- Bridge networks enable communication between containers.
- Docker DNS resolves container names to their network addresses.
- Port publishing exposes container services to the host.
- Containers can communicate without publishing their internal ports.

## Questions and Answers

**1. What does `--network` do?**

Connects a container to a specified Docker network.

**2. How do containers communicate?**

Containers on the same user-defined bridge network can communicate using container names and service ports.

**3. Bridge network vs. host network?**

Bridge networking provides an isolated container network. Host networking shares the host's network stack, subject to platform-specific behavior.

**4. How do you expose a container port?**

Use `-p HOST_PORT:CONTAINER_PORT`, for example `-p 5001:5001`.

## Cleanup
```bash
docker rm -f flask mysql redis
docker network rm my-bridge-net
```

## Expected Outcome
Three containers running on a custom bridge network, with successful Flask API access and verified connectivity to MySQL and Redis.

## Evidence
See the `screenshots/` directory for execution results.

# Exercise 5: Docker Security with AppArmor

## 1. Objective
- Containerize a Python Flask application using Docker.
- Understand AppArmor mandatory access control.
- Prepare a custom AppArmor security profile.
- Use the Python Docker SDK to inspect container security settings.
- Understand how to validate restricted actions.

## 2. Technologies Used
- Python 3
- Flask
- Docker
- AppArmor
- Python Docker SDK

## 3. Application
The Flask application exposes:
- `/` — returns a welcome message.
- `/health` — returns the application health status.

## 4. Docker Implementation
The Dockerfile uses the Python 3.11 slim image, installs Flask, copies the application into `/app`, and exposes port 5000.

Build the image:

```bash
docker build -t flask-apparmor:1.0 .
```

Run the application:

```bash
docker run -d --name flask-apparmor-test -p 5000:5000 flask-apparmor:1.0
```

Test:
- http://localhost:5000
- http://localhost:5000/health

## 5. AppArmor Profile
The `my-apparmor-profile` file contains an illustrative policy intended to restrict access to sensitive files and shell execution while allowing application runtime access.

The policy has not been loaded or validated in this environment. It must be reviewed and tested on a compatible Linux host with AppArmor enabled before being used for enforcement.

## 6. Python Docker SDK
### `apply_apparmor.py`
- Connects to the Docker daemon.
- Inspects Docker security options.
- Avoids claiming AppArmor enforcement when the daemon does not advertise support.
- Includes a conditional path for requesting a profile on a compatible daemon.

### `test_restricted_actions.py`
- Inspects the running container.
- Checks configured security options.
- Reports whether AppArmor enforcement has been verified.

## 7. Test Results
- Flask container started successfully.
- Root endpoint and health endpoint tested successfully.
- Python Docker SDK installed successfully.
- Docker API connection successful.
- Docker security options reported: `seccomp` and `cgroupns`.
- No AppArmor profile configured on the test container.
- Actual AppArmor enforcement and denied-action tests remain unverified.

## 8. Environment Limitation
The exercise was developed on Windows using Docker Desktop and WSL2. The current Docker daemon does not advertise AppArmor support, and the Ubuntu WSL environment reports AppArmor as disabled. Therefore, actual AppArmor enforcement could not be demonstrated.

To complete enforcement testing, use a compatible Linux host or virtual machine with AppArmor enabled. Load and validate the profile there, start the container with the profile attached, and verify expected denials through application tests and system logs.

## 9. Conclusion
The Flask application was containerized successfully, and the Docker SDK scripts were implemented to inspect security configuration. The AppArmor policy was prepared, but enforcement requires validation in a supported Linux environment.



```bash

minikube start

