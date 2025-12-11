# s3bucket

I learned to secure an S3 bucket in this project.  
It was also my first time using AWS.  
The securing was done in **3 steps:** versioning, encryption, and logging.

---

## Prerequisites

To implement these configurations, you need:

- An active AWS account  
- AWS CLI installed and configured  
- Two S3 buckets created in AWS  

---

## Versioning

S3 Versioning is a feature that allows Amazon S3 to keep multiple versions of an object within the same bucket. Instead of overwriting or permanently deleting files, S3 stores each version with a unique version ID. This allows you to recover any previous version at any time.

Enabling versioning is simple: open your bucket, go to the **Properties** tab, and enable **Versioning**.

This feature is essential to protect your data from:

- accidental deletion,  
- mistaken overwrites,  
- malicious actions (ransomware, tampering, insider threats),  
- and for maintaining full audit and historical tracking of object changes.

**In summary:** versioning improves the integrity, availability, and resilience of data stored in S3, making it one of the most effective safeguards for ensuring data continuity in the cloud.

---

## Encryption

S3 Server-Side Encryption (SSE) ensures that all objects stored in your S3 bucket are encrypted at rest. Instead of leaving files in plain text on Amazon’s infrastructure, SSE automatically encrypts your data using managed keys.

To enable it, go to the **Properties** section of your bucket and set the default encryption to **SSE-KMS**, which uses AWS Key Management Service.

Encryption provides:

- protection against unauthorized access,  
- detailed audit logs of key usage,  
- optional key rotation,  
- granular access control for encryption/decryption operations,  
- and compliance with data security standards.

**In summary:** encryption keeps your data confidential, auditable, and secure — a fundamental component of a well-protected S3 environment.

---

## Access Logs

S3 Access Logging records detailed information about every request made to your bucket. Instead of keeping access activity invisible, S3 generates log files containing:

- who accessed the bucket,  
- from where,  
- and what action they performed.

To enable logging, go to your bucket’s **Properties**, open **Server access logging**, and choose a **dedicated log bucket** (you cannot log into the same bucket).

Access logging is useful for:

- detecting suspicious behavior,  
- investigating incidents,  
- tracing unauthorized access attempts,  
- meeting compliance requirements,  
- and enabling long-term monitoring.

**In summary:** access logs increase the traceability and security of your S3 environment, making it easier to monitor activity, detect anomalies, and maintain control over your cloud storage.

---

## Introduction to SIEM

As an additional security measure, I implemented a small log-analysis script that scans S3 access logs and identifies unusual or potentially malicious activity. The script extracts key metadata (IP addresses, HTTP status codes, access patterns) and applies detection rules inspired by cybersecurity best practices.

It flags events such as:

- unknown IP addresses,  
- repeated error-based requests,  
- suspicious access patterns,  
- or potential indicators of compromise (IOCs).

This is a simplified but meaningful introduction to how modern **SIEM (Security Information and Event Management)** systems operate, correlating logs to detect threats and support proactive monitoring and forensic analysis.
