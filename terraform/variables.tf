variable "aws_region" {
  description = "AWS region for the cloud security lab"
  type        = string
  default     = "ap-south-1"
}

variable "admin_ip" {
  description = "Public IPv4 address allowed to access SSH"
  type        = string
}