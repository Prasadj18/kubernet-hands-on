\# Kubernetes Exercise 1 — Hello Pod



\## Objective



Deploy and access an Nginx web application using Kubernetes and Minikube.



\## Technologies



\- Kubernetes

\- Minikube

\- Docker

\- kubectl

\- Nginx



\## Steps



1\. Started Minikube Kubernetes cluster.

2\. Created an Nginx Pod.

3\. Verified the Pod was running.

4\. Exposed the Pod using a NodePort Service.

5\. Accessed the Nginx application through a web browser.



\## Commands



```bash

minikube start

kubectl run hello-k8s --image=nginx --port=80

kubectl get pods

kubectl expose pod hello-k8s --type=NodePort --port=80

minikube service hello-k8s

