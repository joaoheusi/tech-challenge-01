# main.tf



terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "5.17.0" }
  }
  backend "s3" {
    bucket         = "your-terraform-state-bucket-fiap"
    key            = "fastapi-server/terraform.tfstate"
    region         = "sa-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region     = var.aws_region     # You can set this as a variable
  access_key = var.aws_access_key # You can set this as a variable
  secret_key = var.aws_secret_key # You can set this as a variable
}

resource "aws_ecr_repository" "api" {
  name                 = "fastapi-server"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  image_scanning_configuration {
    scan_on_push = true
  }
}

locals {
  repo_url = aws_ecr_repository.api.repository_url
}


# IAM Role for EKS
resource "aws_iam_role" "eks_role" {
  name = "fastapi-eks-role"

  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "eks.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  })
}

# Attach the necessary policies to the EKS role
resource "aws_iam_role_policy_attachment" "eks_policy" {
  role       = aws_iam_role.eks_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

# Output the repository URL
output "ecr_repository_url" {
  value = aws_ecr_repository.api.repository_url
}
