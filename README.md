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



# Exercise 6: Real-Time Operations Monitoring and Alerting
```bash

minikube start


## Objective
Build a real-time monitoring system for a delivery service using Python, Prometheus, Grafana, Docker, and Jenkins.

## Technologies Used
- Python
- Prometheus
- Grafana
- Docker
- Jenkins
- `prometheus-client`

## Project Structure

```text
exercise-06-delivery-monitoring/
├── delivery_metrics.py
├── prometheus.yml
├── alert_rules.yml
├── Jenkinsfile
└── README.md
```

## 1. Delivery Metrics Simulation

The Python application simulates delivery operations and exposes metrics through an HTTP endpoint.

Metrics collected:
- `total_deliveries` — Total deliveries.
- `pending_deliveries` — Pending deliveries.
- `on_the_way_deliveries` — Deliveries in transit.
- `average_delivery_time` — Delivery time observations in seconds.

Install the dependency:

```bash
python -m pip install prometheus-client
```

Run the application:

```bash
python delivery_metrics.py
```

Access the metrics at:

http://localhost:8000/metrics

## 2. Prometheus Configuration

Prometheus scrapes metrics from the Python application every 5 seconds.

Configuration file: `prometheus.yml`

The configuration defines:
- Prometheus self-monitoring.
- Delivery service metrics collection.
- Alert rules file location.

Start Prometheus using Docker:

```powershell
docker run -d --name prometheus `
  -p 9090:9090 `
  --add-host=host.docker.internal:host-gateway `
  -v "${PWD}/prometheus.yml:/etc/prometheus/prometheus.yml" `
  -v "${PWD}/alert_rules.yml:/etc/prometheus/alert_rules.yml" `
  prom/prometheus
```

Access Prometheus at:

http://localhost:9090

Verify targets at:

http://localhost:9090/targets

## 3. Alert Configuration

Configuration file: `alert_rules.yml`

Two alert rules are defined:

- **HighPendingDeliveries:** Triggers when pending deliveries exceed 10 for 15 seconds.
- **HighAverageDeliveryTime:** Triggers when average delivery time exceeds 30 seconds for 15 seconds.

View alerts at:

http://localhost:9090/alerts

## 4. Grafana Dashboard

Grafana visualizes delivery metrics collected by Prometheus.

Start Grafana:

```powershell
docker run -d --name grafana -p 3000:3000 grafana/grafana
```

Access Grafana at:

http://localhost:3000

Default login for a fresh instance:
- Username: `admin`
- Password: `admin`

Configure Prometheus as a data source using:

```text
http://host.docker.internal:9090
```

Create dashboard panels for:
1. Total Deliveries
2. Pending Deliveries
3. On-the-Way Deliveries
4. Average Delivery Time

Average delivery time query:

```promql
average_delivery_time_sum / average_delivery_time_count
```

## 5. Jenkins Pipeline

The `Jenkinsfile` defines pipeline stages for checking Docker availability, preparing the workspace, building the application image, running the application, and starting Prometheus and Grafana.

Jenkins can be started using Docker:

```powershell
docker run -d --name jenkins `
  -p 8080:8080 `
  -p 50000:50000 `
  -v jenkins_home:/var/jenkins_home `
  jenkins/jenkins:lts
```

Access Jenkins at:

http://localhost:8080

The pipeline requires a valid `Jenkinsfile`, a configured Jenkins job, and access to the Docker daemon. The pipeline should be tested in the target environment before claiming successful automated execution.

## 6. Testing and Verification

- Verified the Python metrics endpoint at port 8000.
- Confirmed that Prometheus started successfully.
- Confirmed the `delivery_service` and `prometheus` targets were **UP**.
- Configured alert rules for pending deliveries and delivery time.
- Grafana dashboard and Jenkins pipeline require verification after setup.

## Conclusion

This project demonstrates delivery metrics collection, Prometheus monitoring, alert rule configuration, Grafana visualization, and Jenkins-based pipeline automation. It provides a foundation for detecting operational issues and monitoring delivery performance in real time.


# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins

## Objective
To understand Continuous Integration (CI), learn Jenkins installation and configuration, and demonstrate a basic CI pipeline.

## 1. What is Continuous Integration?

Continuous Integration is a software development practice in which developers frequently integrate code changes into a shared repository. Automated builds and tests help detect errors early and improve software quality.

### Key Features
- Frequent code integration
- Automated builds
- Automated testing
- Immediate feedback

### Benefits
- Early bug detection
- Improved collaboration
- Faster development cycles
- Improved software quality

## 2. CI Workflow

1. Developer pushes code to a Git repository.
2. The CI server detects code changes.
3. The build process is triggered.
4. Automated tests are executed.
5. Results are reported to the developer.

## 3. Introduction to Jenkins

Jenkins is an open-source automation server used to automate software building, testing, and deployment. It supports CI/CD through pipelines and plugins.

### Key Jenkins Concepts
- **Job/Project:** A task executed by Jenkins.
- **Build:** Execution of a configured process.
- **Pipeline:** A sequence of automated stages.
- **Plugins:** Extend Jenkins functionality.
- **Nodes:** Machines on which Jenkins jobs execute.

## 4. Jenkins Installation Using Docker

Run Jenkins using Docker:

```bash
docker run -d --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  jenkins/jenkins:lts
```

Verify the container:

```bash
docker ps
```

Access Jenkins at:

http://localhost:8080

For a fresh installation, retrieve the initial administrator password:

```bash
docker exec -it jenkins bash
cat /var/jenkins_home/secrets/initialAdminPassword
```

Use the password on the Jenkins setup page to complete the initial configuration.

## 5. Practical CI Pipeline

A Jenkins Pipeline named `Exercise-7-CI` was created and executed successfully.

### Pipeline Stages
1. **Checkout:** Retrieves the source code.
2. **Build:** Executes the build step.
3. **Test:** Runs the configured tests.
4. **CI Success:** Confirms successful completion.

### Execution Result
- Pipeline created successfully.
- Build #1 executed successfully.
- All configured pipeline stages completed successfully.

## 6. Result

Successfully understood Continuous Integration, installed Jenkins using Docker, and demonstrated a basic CI pipeline with checkout, build, test, and success stages.

## Conclusion

Jenkins automates repetitive development tasks and provides feedback on code changes. Continuous Integration helps teams identify problems early and maintain software quality.


# Exercise 8: Creating a Hello World Jenkins Job

## Objective
To create a simple shell script, push it to GitHub, and configure a Jenkins Freestyle job to execute the script automatically.

## Technologies Used
- Jenkins
- Docker
- Git
- GitHub
- Bash Shell Scripting

## 1. Create the Shell Script

Create a file named `hello-world.sh` with the following content:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

The script prints a greeting message when executed.

## 2. Push the Script to GitHub

Initialize a Git repository and commit the script:

```bash
git init
git add hello-world.sh
git commit -m "Add hello-world.sh"
```

Connect the local repository to GitHub:

```bash
git remote add origin https://github.com/<your-username>/devops-sample-code.git
git branch -M main
git push -u origin main
```

Replace `<your-username>` with your GitHub username.

## 3. Start Jenkins Using Docker

Run Jenkins:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

Verify the container:

```bash
docker ps
```

Access Jenkins at:

http://localhost:8080

For a fresh Jenkins installation, retrieve the initial administrator password:

```bash
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Complete the initial setup and log in.

## 4. Create a Jenkins Freestyle Job

1. Open the Jenkins dashboard.
2. Click **New Item**.
3. Enter the job name `HelloWorld`.
4. Select **Freestyle project** and click **OK**.
5. Under **Source Code Management**, select **Git**.
6. Enter the GitHub repository URL.
7. Under **Build Steps**, select **Execute shell**.
8. Add the command:

```bash
sh hello-world.sh
```

9. Save the job.

**Note:** The Execute shell step requires a Jenkins environment that supports shell commands, such as the Linux-based Jenkins container.

## 5. Execute the Job

1. Open the `HelloWorld` job.
2. Click **Build Now**.
3. Open the build number.
4. Select **Console Output**.

Expected output:

```text
+ echo 'Hello, Jenkins!'
Hello, Jenkins!
Finished: SUCCESS
```

## Result
Successfully demonstrated how to store a shell script in GitHub and configure a Jenkins Freestyle job to execute it.

## Conclusion
Jenkins simplifies task automation by executing scripts through configured jobs. Integrating Jenkins with GitHub provides a foundation for automated build and test workflows.


# Exercise 9: Jenkins Multi-Stage Pipeline for Python Flask Application

## Objective
To create and execute a Jenkins Pipeline that automates the build, test, deployment, and execution of a Python Flask application.

## Technologies Used
- Python
- Flask
- Jenkins
- Docker
- Git and GitHub
- Python unittest

## Project Structure

```text
exercise-09-jenkins-multistage-pipeline/
├── app.py
├── requirements.txt
├── test_app.py
├── Jenkinsfile
└── README.md
```

## 1. Python Flask Application

The application is defined in `app.py` and exposes a home endpoint (`/`).

Expected response:

```text
Hello, Jenkins Multi-Stage Pipeline!
```

## 2. Dependencies

The `requirements.txt` file specifies Flask as the application dependency.

Install dependencies using:

```bash
python3 -m pip install -r requirements.txt
```

## 3. Unit Testing

The `test_app.py` file uses Python's `unittest` framework and Flask's test client to verify the home endpoint.

Run the tests:

```bash
python3 -m unittest discover -s .
```

The test checks that the endpoint returns HTTP status code 200 and the expected response message.

## 4. Jenkins Pipeline

The `Jenkinsfile` defines these stages:

1. **Build** — prepares the application environment and dependencies.
2. **Test** — executes the unit tests.
3. **Deploy** — copies `app.py` into the mock deployment directory.
4. **Run Application** — starts the Flask application.
5. **Test Application** — executes the application tests again.

The pipeline includes post-build messages for success and failure.

## 5. Configure Jenkins

1. Start Jenkins and open `http://localhost:8080`.
2. Create a new item named `Python-MultiStage-Pipeline`.
3. Select **Pipeline**.
4. Under Pipeline, select **Pipeline script from SCM**.
5. Choose Git and enter the GitHub repository URL.
6. Set the branch to `main` and the script path to `Jenkinsfile`.
7. Save and click **Build Now**.

## 6. Expected Results

- Dependencies are available to the application.
- Unit tests pass.
- The application file is copied to the deployment directory.
- The Flask application starts.
- Application tests pass.
- Jenkins reports a successful pipeline execution.

## 7. Additional Enhancements

- Add a code quality stage using Flake8 or Pylint.
- Build and deploy the application as a Docker container.
- Add email or Slack notifications for pipeline results.

## Conclusion

This exercise demonstrates how Jenkins automates multiple stages of a Python application's development workflow, including testing, deployment, and application verification.
