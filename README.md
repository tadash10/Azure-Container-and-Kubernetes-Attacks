# Azure Container and Kubernetes Attacks

## Description

This Python script is designed for offensive security testing in Azure environments, specifically targeting Azure Kubernetes Service (AKS), Azure Container Instances (ACI), and Azure Container Registry (ACR). It provides various functions to assess container and Kubernetes security, simulate attacks, and generate reports.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Azure-Container-and-Kubernetes-Attacks.git

   
Navigate to the project directory:
cd Azure-Container-and-Kubernetes-Attacks


Create a virtual environment (optional but recommended):
python -m venv venv

Activate the virtual environment:

    On Windows:venv\Scripts\activate

On macOS and Linux: source venv/bin/activate

Install the required dependencies:
pip install -r requirements.txt

    You may need to install additional tools and dependencies based on your testing requirements. Ensure you have Docker, Kubernetes tools, and other necessary software installed.

Usage

The script provides several functions to assess Azure container and Kubernetes security. Use the following command-line options to execute specific functions:

    --aks: Scan Azure Kubernetes Service (AKS) clusters for vulnerabilities and security weaknesses.
    --aci: Scan Azure Container Instances (ACI) for vulnerabilities and misconfigurations.
    --acr: Scan Azure Container Registry (ACR) for container image vulnerabilities.
    --exploit: Integrate with known container and Kubernetes exploits to test vulnerabilities and perform automated exploitation (for educational and testing purposes).
    --credentials: Test default or weak credentials against Azure services, including AKS, ACI, and ACR.
    --image-scan: Scan container images in Azure Container Registry for vulnerabilities, including outdated software and known CVEs.
    --escalation: Perform privilege escalation tests within Azure containers and Kubernetes clusters.
    --exfiltration: Test data exfiltration techniques from compromised containers or clusters.
    --lateral-movement: Simulate lateral movement within an AKS cluster (for educational and testing purposes).
    --report: Generate a detailed security report with findings, risk assessments, and remediation suggestions.
    --container-breakout: Attempt container breakout techniques to escalate privileges within Kubernetes clusters.
    --cleanup: Automatically clean up resources and containers created during testing to avoid unintended impact on the Azure environment.

Examples

    Scan AKS clusters for vulnerabilities:

    bash

python azure_security.py --aks

Scan ACI instances for vulnerabilities:

bash

python azure_security.py --aci

Scan ACR registry for container image vulnerabilities:

bash

python azure_security.py --acr

Generate a security report after running multiple tests:

bash

    python azure_security.py --aks --aci --acr --report

Functions

    Scan AKS Clusters (--aks): This function scans Azure Kubernetes Service clusters for vulnerabilities, security weaknesses, and misconfigurations.

    Scan ACI Instances (--aci): It scans Azure Container Instances for vulnerabilities, misconfigurations, and potential security issues.

    Scan ACR Registry (--acr): This function scans container images in Azure Container Registry for vulnerabilities, including outdated software and known CVEs.

    Exploit Integration (--exploit): Integrates with known container and Kubernetes exploits to test vulnerabilities and perform automated exploitation (for educational and testing purposes).

    Credential Testing (--credentials): Tests default or weak credentials against Azure services, including AKS, ACI, and ACR.

    Container Image Scanning (--image-scan): Scans container images in Azure Container Registry for vulnerabilities, helping to identify potential security risks.

    Privilege Escalation Tests (--escalation): Performs privilege escalation tests within Azure containers and Kubernetes clusters to identify potential security weaknesses.

    Exfiltration Tests (--exfiltration): Tests data exfiltration techniques from compromised containers or clusters, highlighting potential data breaches.

    Lateral Movement Simulation (--lateral-movement): Simulates lateral movement within an AKS cluster (for educational and testing purposes).

    Reporting (--report): Generates a detailed security report with findings, risk assessments, and remediation suggestions based on the tests performed.

    Container Breakout Techniques (--container-breakout): Attempts container breakout techniques to escalate privileges within Kubernetes clusters, showcasing the risks associated with misconfigured security contexts.

    Automated Cleanup (--cleanup): Automatically cleans up resources and containers created during testing to ensure no unintended impact on the Azure environment.

    


