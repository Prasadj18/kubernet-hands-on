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
