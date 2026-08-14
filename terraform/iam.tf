resource "aws_iam_policy" "s3_read_only" {
  name        = "CloudLab-S3-ReadOnly"
  description = "Least-privilege policy for reading objects from the cloud security lab bucket"

  policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Action = [
          "s3:GetObject"
        ]

        Resource = "${aws_s3_bucket.security_lab.arn}/*"
      }
    ]
  })
}

data "aws_caller_identity" "current" {}

resource "aws_iam_role" "s3_reader" {
  name = "CloudLab-S3-Reader"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          AWS = data.aws_caller_identity.current.arn
        }

        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "s3_reader" {
  role       = aws_iam_role.s3_reader.name
  policy_arn = aws_iam_policy.s3_read_only.arn
}