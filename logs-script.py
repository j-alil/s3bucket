import os
import gzip
import boto3
from dotenv import load_dotenv

load_dotenv()

LOG_BUCKET = os.getenv("LOG_BUCKET_NAME")
REGION = os.getenv("AWS_REGION")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
allowed_ips_raw = os.getenv("ALLOWED_IPS", "")
ALLOWED_IPS = [ip.strip() for ip in allowed_ips_raw.split(",") if ip.strip()]


s3 = boto3.client(
    "s3",
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

# --- anomaly detection rules ---
def is_suspicious(line):
    #return true if a log line appears suspicious based on rules.
    parts = line.split()
    if len(parts) < 10:
        return False  

    ip = parts[4]       
    status = parts[8]    

    if ALLOWED_IPS and ip not in ALLOWED_IPS:
        return True

    if status.startswith("4") or status.startswith("5"):
        return True

    return False

# --- log scanning ---
def scan_logs():
    #scan logs in the S3 bucket by calling is_suspicious on each line
    anomalies = []

    print(f"Scanning logs in bucket: {LOG_BUCKET}\n")

    objects = s3.list_objects_v2(Bucket=LOG_BUCKET)

    for obj in objects.get("Contents", []):
        key = obj["Key"]

        local_file = "tmp.gz"
        s3.download_file(LOG_BUCKET, key, local_file)

        with gzip.open(local_file, "rt") as f:
            for line in f:
                if is_suspicious(line):
                    anomalies.append({
                        "line": line.strip(),
                        "file": key
                    })

    return anomalies

if __name__ == "__main__":
    findings = scan_logs()

    print("=== Suspicious Activity Report ===\n")

    if not findings:
        print("No suspicious activity detected.")
    else:
        for f in findings:
            print(f"Suspicious line in {f['file']}:\n  {f['line']}\n")
