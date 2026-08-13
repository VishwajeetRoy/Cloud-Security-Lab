output "security_lab_bucket_name" {
  description = "Name of the security lab S3 bucket"
  value       = aws_s3_bucket.security_lab.bucket
}

output "security_lab_bucket_arn" {
  description = "ARN of the security lab S3 bucket"
  value       = aws_s3_bucket.security_lab.arn
}