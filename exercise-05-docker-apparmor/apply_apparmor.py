import docker
from docker.errors import DockerException, APIError

IMAGE_NAME = "flask-apparmor:1.0"
CONTAINER_NAME = "flask-apparmor-secure"
APPARMOR_PROFILE = "my-apparmor-profile"


def main():
    try:
        client = docker.from_env()
        client.ping()

        print("Connected to Docker successfully.")

        info = client.info()
        security_options = info.get("SecurityOptions", [])

        print("\nDocker security options:")
        for option in security_options:
            print(f"- {option}")

        apparmor_supported = any(
            "apparmor" in option.lower()
            for option in security_options
        )

        if not apparmor_supported:
            print(
                "\nAppArmor is not advertised by this Docker daemon."
            )
            print(
                "The container will NOT be launched with a claim "
                "of AppArmor enforcement."
            )
            return

        print(f"\nStarting container with profile: {APPARMOR_PROFILE}")

        container = client.containers.run(
            IMAGE_NAME,
            name=CONTAINER_NAME,
            detach=True,
            ports={"5000/tcp": 5001},
            security_opt=[
                f"apparmor={APPARMOR_PROFILE}"
            ],
        )

        print(f"Container started: {container.short_id}")
        print("Test the app at http://localhost:5001")

    except APIError as error:
        print(f"Docker API error: {error}")
    except DockerException as error:
        print(f"Could not connect to Docker: {error}")


if __name__ == "__main__":
    main()