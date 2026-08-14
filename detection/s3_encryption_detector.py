import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "cloud-security-lab-vishwajeet-2026"


def check_encryption_enforcement():
    s3 = boto3.client("s3")

    try:
        response = s3.get_bucket_policy(Bucket=BUCKET_NAME)
        policy = response["Policy"]

        required_control = "DenyUnencryptedObjectUploads"

        if required_control in policy:
            print("[PASS] S3 encryption enforcement policy is configured.")
            return 0

        print("[HIGH] S3 Encryption Enforcement Misconfiguration Detected")
        print(f"Bucket: {BUCKET_NAME}")
        print("Finding:")
        print("  - Required encryption enforcement policy is missing.")

        print(
            "\nRisk: The bucket lacks the expected policy-level "
            "enforcement for SSE-S3 upload requests."
        )
        print(
            "Recommendation: Restore the encryption enforcement "
            "bucket policy."
        )

        return 1

    except ClientError as error:
        error_code = error.response["Error"]["Code"]

        if error_code == "NoSuchBucketPolicy":
            print("[HIGH] S3 Encryption Enforcement Misconfiguration Detected")
            print(f"Bucket: {BUCKET_NAME}")
            print("Finding:")
            print("  - No bucket policy exists.")

            print(
                "\nRisk: The expected encryption enforcement control "
                "is missing."
            )
            print(
                "Recommendation: Restore the encryption enforcement "
                "bucket policy."
            )

            return 1

        raise


if __name__ == "__main__":
    raise SystemExit(check_encryption_enforcement())