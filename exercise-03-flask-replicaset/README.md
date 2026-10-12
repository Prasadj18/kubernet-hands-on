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