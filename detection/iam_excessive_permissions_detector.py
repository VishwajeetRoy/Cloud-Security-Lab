import boto3

POLICY_ARN = (
    "arn:aws:iam::"
    + boto3.client("sts").get_caller_identity()["Account"]
    + ":policy/CloudLab-S3-ReadOnly"
)


def check_policy():
    iam = boto3.client("iam")

    policy = iam.get_policy(PolicyArn=POLICY_ARN)
    version_id = policy["Policy"]["DefaultVersionId"]

    response = iam.get_policy_version(
        PolicyArn=POLICY_ARN,
        VersionId=version_id
    )

    document = response["PolicyVersion"]["Document"]

    findings = []

    statements = document.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]

    for statement in statements:
        if statement.get("Effect") != "Allow":
            continue

        actions = statement.get("Action", [])
        resources = statement.get("Resource", [])

        if isinstance(actions, str):
            actions = [actions]

        if isinstance(resources, str):
            resources = [resources]

        if "*" in actions:
            findings.append("Wildcard Action (*)")

        if "*" in resources:
            findings.append("Wildcard Resource (*)")

    if findings:
        print("[CRITICAL] Excessive IAM Permissions Detected")
        print(f"Policy: CloudLab-S3-ReadOnly")
        print("Findings:")

        for finding in findings:
            print(f"  - {finding}")

        print("\nRisk: The policy grants permissions beyond least privilege.")
        print("Recommendation: Restrict actions and resources to only what is required.")

        return 1

    print("[PASS] IAM policy follows the expected least-privilege checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check_policy())