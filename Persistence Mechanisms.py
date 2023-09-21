import subprocess

def establish_persistence(container_id, persistence_command):
    try:
        # Execute a command to establish persistence within the container
        command = f"/bin/bash -c '{persistence_command}'"
        subprocess.run(f"docker exec -it {container_id} {command}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to establish persistence: {e}")
    except Exception as e:
        print(f"Error during establishing persistence: {e}")

# Example usage
container_id = "container_id_to_persist"
persistence_command = "persistence_command_here"
establish_persistence(container_id, persistence_command)
