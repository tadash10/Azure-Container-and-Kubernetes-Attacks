import json

def generate_security_report(findings, recommendations):
    try:
        # Generate a JSON security report with findings and remediation suggestions
        report_data = {
            "findings": findings,
            "recommendations": recommendations
        }
        with open("security_report.json", "w") as report_file:
            json.dump(report_data, report_file, indent=4)
        print("Security report generated: security_report.json")
    except Exception as e:
        print(f"Error while generating the security report: {e}")

# Example usage
findings = ["Vulnerability in AKS cluster", "Weak ACI access controls"]
recommendations = ["Apply security patches", "Review and tighten ACI permissions"]
generate_security_report(findings, recommendations)
