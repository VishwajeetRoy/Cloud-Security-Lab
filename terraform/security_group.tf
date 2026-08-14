resource "aws_security_group" "cloud_lab" {
  name        = "cloud-lab-secure-sg"
  description = "Secure security group for the cloud security lab"

  ingress {
    description = "SSH from the lab administrator IP"
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = ["${var.admin_ip}/32"]
  }

  ingress {
    description = "HTTP access"
    protocol    = "tcp"
    from_port   = 80
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "Cloud-Lab-Secure-SG"
    Environment = "Lab"
  }
}