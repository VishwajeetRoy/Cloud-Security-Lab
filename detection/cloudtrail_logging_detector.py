import boto3

TRAIL_NAME = "cloud-security-lab-trail"


def check_cloudtrail_logging():
    cloudtrail = boto3.client("cloudtrail")

    try:
        status = cloudtrail.get_trail_status(Name=TRAIL_NAME)

        if status.get("IsLogging"):
            print("[PASS] CloudTrail logging is enabled.")
            print(f"Trail: {TRAIL_NAME}")
            return 0

        print("[HIGH] CloudTrail Logging Misconfiguration Detected")
        print(f"Trail: {TRAIL_NAME}")
        print("Finding:")
        print("  - CloudTrail logging is currently stopped.")

        print(
            "\nRisk: AWS management activity may not be recorded "
            "while CloudTrail logging is disabled."
        )
        print(
            "Recommendation: Restore CloudTrail logging immediately."
        )

        return 1

    except cloudtrail.exceptions.TrailNotFoundException:
        print("[HIGH] CloudTrail Trail Not Found")
        print(f"Trail: {TRAIL_NAME}")
        print(
            "Recommendation: Restore the expected CloudTrail trail."
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(check_cloudtrail_logging())