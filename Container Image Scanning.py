import subprocess

def scan_container_image(image_name):
    try:
        # Use a container image scanning tool to assess vulnerabilities
        command = f"container-scanner {image_name}"
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Image scanning failed: {e}")
    except Exception as e:
        print(f"Error during image scanning: {e}")

# Example usage
image_name = "azure-container-image:latest"
scan_container_image(image_name)
