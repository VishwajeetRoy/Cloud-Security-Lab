import boto3

BUCKET_NAME = "cloud-security-lab-vishwajeet-2026"


def check_public_access():
    s3 = boto3.client("s3")

    try:
        response = s3.get_public_access_block(Bucket=BUCKET_NAME)
        config = response["PublicAccessBlockConfiguration"]

        checks = {
            "BlockPublicAcls": config.get("BlockPublicAcls", False),
            "IgnorePublicAcls": config.get("IgnorePublicAcls", False),
            "BlockPublicPolicy": config.get("BlockPublicPolicy", False),
            "RestrictPublicBuckets": config.get("RestrictPublicBuckets", False),
        }

        failed = [name for name, enabled in checks.items() if not enabled]

        if failed:
            print("[HIGH] S3 Public Access Protection Misconfiguration")
            print(f"Bucket: {BUCKET_NAME}")
            print("Failed controls:")

            for control in failed:
                print(f"  - {control}: DISABLED")

            print("\nRisk: The bucket lacks S3 public-access protection.")
            print("Recommendation: Enable all four public-access block controls.")

            return 1

        print("[PASS] S3 public-access protection is securely configured.")
        return 0

    except s3.exceptions.NoSuchPublicAccessBlockConfiguration:
        print("[HIGH] S3 Public Access Protection Misconfiguration")
        print(f"Bucket: {BUCKET_NAME}")
        print("No public-access block configuration exists.")
        return 1


if __name__ == "__main__":
    raise SystemExit(check_public_access())