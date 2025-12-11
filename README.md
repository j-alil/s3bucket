# s3bucket
I learned to secure a s3 bucket in this project.  
It was also my first time using AWS.  
The securing was done in 3 steps : versioning, encryption and logs  

## Prerequisites 
If you want to implement these things, you need to set up :
        - An active AWS account
        - AWS CLI installed and configured
        - Two S3 buckets created in AWS

## Versioning
S3 Versioning is a feature that allows Amazon S3 to keep multiple versions of an object within the same bucket. Instead of overwriting or deleting files permanently, S3 stores each version with a unique version ID. This makes it possible to recover previous versions of objects at any time.  
To enable it, you just have to go in the **Properties** section of your bucket which is really simple.  
That simple feature is really important to prevent your buckets from accidental deletion and mistaken overwrites in the first sight. But you also need it for malicious actions like ransomware, data tampering, or insider threats. Finally, you'll need it for audits and historical tracking to get a complete history of changes to objects.  
In summary, versioning enhances the integrity, availability, and resilience of the data stored in S3. It is one of the simplest yet most effective safeguards for preserving data continuity in the cloud.  

## Encryption  
S3 Server-Side Encryption (SSE) is a mechanism that ensures all objects stored in an Amazon S3 bucket are encrypted at rest. Instead of leaving files in plain text on Amazon’s infrastructure, SSE automatically encrypts your data using managed encryption keys. When enabling it, you simply go to the **Properties** section of your bucket, and set encryption to **SSE-KMS**, which uses AWS Key Management Service.  
This feature is essential because it protects your stored data from unauthorized access even if someone gains access to the underlying storage. With SSE-KMS, you also benefit from detailed audit logs, key rotation options, and granular permissions to control who can encrypt or decrypt objects.  
Finally, encryption helps meet compliance requirements and strengthens overall data confidentiality within your S3 buckets.
In summary, encryption ensures that your data remains confidential, auditable, and secure, making it a fundamental component of a well-protected cloud storage environment.

## Access Logs
S3 Access Logging is a feature that records detailed information about every request made to your bucket. Instead of leaving access activity invisible, S3 generates log files that capture who accessed the bucket, from where, and what action they performed. To enable it, you simply go to the **Properties** section of your bucket, scroll down to **Server access logging**, and choose a dedicated target bucket where logs will be stored (you can't use the same bucket to store the logs).  
This feature is useful because it gives you full visibility into the interactions with your bucket. It allows you to detect suspicious behavior, investigate security incidents, and trace unauthorized or unexpected access attempts. Access logs are also extremely useful for compliance audits and long-term monitoring, as they provide a transparent record of all operations on your data.  
In summary, access logging strengthens the traceability and security of your S3 environment, making it easier to monitor activity, detect anomalies, and maintain full control over your cloud storage.  

## Introduction to SIEM
As an additional security measure, I implemented a small log-analysis script designed to scan S3 access logs and identify unusual or potentially malicious activity. The script parses each log entry, extracts key metadata such as IP addresses and HTTP status codes, and applies detection rules based on common cybersecurity practices. It flags events such as unknown source IPs, repeated error-based requests, or access patterns that may indicate reconnaissance, brute-force attempts, or indicators of compromise (IOCs). This type of anomaly detection represents a simplified but meaningful introduction to how modern SIEM (Security Information and Event Management) systems operate.
