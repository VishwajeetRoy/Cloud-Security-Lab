terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "security_lab" {
  bucket = "cloud-security-lab-vishwajeet-2026"

  tags = {
    Name        = "Cloud Security Lab"
    Environment = "Lab"
    Purpose     = "Security Monitoring and Misconfiguration Detection"
  }
}

resource "aws_s3_bucket_public_access_block" "security_lab" {
  bucket = aws_s3_bucket.security_lab.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_ownership_controls" "security_lab" {
  bucket = aws_s3_bucket.security_lab.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "security_lab" {
  bucket = aws_s3_bucket.security_lab.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "security_lab" {
  bucket = aws_s3_bucket.security_lab.id

  versioning_configuration {
    status = "Enabled"
  }
}