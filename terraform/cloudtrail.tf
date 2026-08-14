resource "aws_cloudtrail" "security_lab" {
  name                          = "cloud-security-lab-trail"
  s3_bucket_name                = aws_s3_bucket.security_lab.id
  s3_key_prefix                 = "cloudtrail"
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true

  event_selector {
    read_write_type           = "All"
    include_management_events = true
  }

  tags = {
    Name        = "Cloud Security Lab Trail"
    Environment = "Lab"
    Purpose     = "Security Monitoring and Audit Logging"
  }
}