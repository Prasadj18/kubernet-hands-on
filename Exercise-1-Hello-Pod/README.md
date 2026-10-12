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
