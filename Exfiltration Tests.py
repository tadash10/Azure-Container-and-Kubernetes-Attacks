import subprocess

def test_data_exfiltration(container_id, exfiltration_command):
    try:
        # Execute a command to test data exfiltration
        command = f"/bin/bash -c '{exfiltration_command}'"
        subprocess.run(f"docker exec -it {container_id} {command}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Data exfiltration test failed: {e}")
    except Exception as e:
        print(f"Error during data exfiltration test: {e}")

# Example usage
container_id = "container_id_to_test"
exfiltration_command = "exfiltration_command_here"
test_data_exfiltration(container_id, exfiltration_command)
