resource "aws_s3_bucket_policy" "encryption_enforcement" {
  bucket = aws_s3_bucket.security_lab.id

  policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Sid       = "DenyUnencryptedObjectUploads"
        Effect    = "Deny"
        Principal = "*"

        Action   = "s3:PutObject"
        Resource = "${aws_s3_bucket.security_lab.arn}/*"

        Condition = {
          StringNotEquals = {
            "s3:x-amz-server-side-encryption" = "AES256"
          }
        }
      }
    ]
  })
}