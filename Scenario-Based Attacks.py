import subprocess

def simulate_lateral_movement(aks_cluster, compromised_node):
    try:
        # Simulate lateral movement within an AKS cluster
        command = f"kubectl exec -it {compromised_node} -- /bin/bash"
        subprocess.run(f"kubectl --context {aks_cluster} {command}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Lateral movement failed: {e}")
    except Exception as e:
        print(f"Error during lateral movement simulation: {e}")

# Example usage
aks_cluster = "aks-cluster-name"
compromised_node = "compromised-node-name"
simulate_lateral_movement(aks_cluster, compromised_node)
