
import docker
from docker.errors import DockerException


def main():
    try:
        client = docker.from_env()
        client.ping()

        print("Connected to Docker successfully.")

        security_options = client.info().get("SecurityOptions", [])

        print("\nDocker security options:")
        for option in security_options:
            print(f"- {option}")

        apparmor_supported = any(
            "apparmor" in option.lower()
            for option in security_options
        )

        try:
            container = client.containers.get("flask-apparmor-test")
            container.reload()

            print("\nContainer details:")
            print(f"Name: {container.name}")
            print(f"Status: {container.status}")

            host_config = container.attrs.get("HostConfig", {})
            security_opt = host_config.get("SecurityOpt") or []

            print(f"Configured security options: {security_opt}")

            profile_configured = any(
                "apparmor=" in option.lower()
                for option in security_opt
            )

            print(f"AppArmor profile configured: {profile_configured}")

        except docker.errors.NotFound:
            print("\nContainer 'flask-apparmor-test' was not found.")
            print("Start the Flask test container before inspecting it.")

        print("\nRestricted action test status:")
        if apparmor_supported:
            print(
                "AppArmor appears in Docker security options. "
                "Further profile and denial tests are required."
            )
        else:
            print(
                "NOT VERIFIED: Docker does not advertise AppArmor. "
                "Reading /etc/passwd or executing /bin/bash alone "
                "would not prove AppArmor enforcement."
            )

    except DockerException as error:
        print(f"Docker error: {error}")


if __name__ == "__main__":
    main()
