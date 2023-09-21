import requests

def discover_azure_apis(target_aks, target_aci):
    try:
        # Discover exposed APIs and services within Azure AKS and ACI
        aks_apis = requests.get(f"https://{target_aks}/apis")
        aci_apis = requests.get(f"https://{target_aci}/v1")
        
        # Process and analyze API responses to identify potential attack surfaces
        if aks_apis.status_code == 200:
            print("Discovered AKS APIs:")
            print(aks_apis.text)
        if aci_apis.status_code == 200:
            print("Discovered ACI APIs:")
            print(aci_apis.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during API discovery: {e}")

# Example usage
target_aks = "azure-aks-url.com"
target_aci = "azure-aci-url.com"
discover_azure_apis(target_aks, target_aci)
