# main.tf

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "The AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "aws_account_id" {
  description = "The AWS account ID where the resources are created"
  type        = string
}

# ECR Repository
resource "aws_ecr_repository" "api" {
  name                 = "fastapi-server"
  image_tag_mutability = "MUTABLE"
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

# Pass variables to be used by the GitHub Action
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# This ensures the correct region and account ID are used
locals {
  aws_region  = var.aws_region
  account_id  = var.aws_account_id
}

# Define the backend for storing the Terraform state file
# Uncomment and configure if you want to use a remote backend (e.g., S3)
# terraform {
#   backend "s3" {
#     bucket = "your-terraform-state-bucket"
#     key    = "path/to/your/terraform.tfstate"
#     region = var.aws_region
#   }
# }
