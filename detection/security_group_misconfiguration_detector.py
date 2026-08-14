import boto3

SECURITY_GROUP_NAME = "cloud-lab-secure-sg"


def check_security_group():
    ec2 = boto3.client("ec2")

    response = ec2.describe_security_groups(
        Filters=[
            {
                "Name": "group-name",
                "Values": [SECURITY_GROUP_NAME]
            }
        ]
    )

    security_groups = response["SecurityGroups"]

    if not security_groups:
        print("[HIGH] Security Group not found")
        return 1

    findings = []

    for security_group in security_groups:
        for rule in security_group.get("IpPermissions", []):
            if (
                rule.get("IpProtocol") == "tcp"
                and rule.get("FromPort") == 22
                and rule.get("ToPort") == 22
            ):
                for ip_range in rule.get("IpRanges", []):
                    if ip_range.get("CidrIp") == "0.0.0.0/0":
                        findings.append(
                            "SSH (TCP 22) exposed to 0.0.0.0/0"
                        )

    if findings:
        print("[HIGH] Security Group Misconfiguration Detected")
        print(f"Security Group: {SECURITY_GROUP_NAME}")
        print("Findings:")

        for finding in findings:
            print(f"  - {finding}")

        print(
            "\nRisk: SSH is accessible from any IPv4 address."
        )
        print(
            "Recommendation: Restrict SSH access to a trusted IP range."
        )

        return 1

    print("[PASS] Security Group follows the expected network security checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check_security_group())