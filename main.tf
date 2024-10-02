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
  region     = var.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

# ECR Repository
resource "aws_ecr_repository" "api" {
  name                 = "fastapi-server"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  image_scanning_configuration {
    scan_on_push = true
  }
}

# IAM Role for EKS
resource "aws_iam_role" "eks_role" {
  name = "fastapi-eks-role"

  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": { "Service": "eks.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }]
  })
}

# Attach the necessary policies to the EKS role
resource "aws_iam_role_policy_attachment" "eks_policy" {
  role       = aws_iam_role.eks_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

# VPC
resource "aws_vpc" "eks_vpc" {
  cidr_block = "10.0.0.0/16"
}

# Subnets
resource "aws_subnet" "eks_subnet_a" {
  vpc_id            = aws_vpc.eks_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "sa-east-1a"
}

resource "aws_subnet" "eks_subnet_b" {
  vpc_id            = aws_vpc.eks_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "sa-east-1b"
}

# Security Group
resource "aws_security_group" "eks_sg" {
  name        = "eks-cluster-sg"
  description = "Security group for EKS cluster"
  vpc_id      = aws_vpc.eks_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EKS Cluster
resource "aws_eks_cluster" "fastapi_cluster" {
  name     = "fastapi-cluster"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids         = [aws_subnet.eks_subnet_a.id, aws_subnet.eks_subnet_b.id]
    security_group_ids = [aws_security_group.eks_sg.id]
  }

  depends_on = [aws_iam_role_policy_attachment.eks_policy]
}

# Node Group for EKS
resource "aws_eks_node_group" "fastapi_node_group" {
  cluster_name    = aws_eks_cluster.fastapi_cluster.name
  node_group_name = "fastapi-node-group"
  node_role_arn   = aws_iam_role.eks_node_role.arn
  subnet_ids      = [aws_subnet.eks_subnet_a.id, aws_subnet.eks_subnet_b.id]

  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }

  instance_types = ["t3.small"]

  disk_size = 20

  remote_access {
    ec2_ssh_key = "your-ssh-key-name"  # Replace with your key name if needed
  }

  # Enable monitoring and tags for nodes
  ami_type = "AL2_x86_64"

  tags = {
    Environment = "production"
  }
}

# IAM Role for EKS Worker Nodes
resource "aws_iam_role" "eks_node_role" {
  name = "fastapi-node-role"

  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "ec2.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  })
}

# Attach necessary policies to the EKS Node Role
resource "aws_iam_role_policy_attachment" "eks_node_policy" {
  role       = aws_iam_role.eks_node_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}

resource "aws_iam_role_policy_attachment" "eks_cni_policy" {
  role       = aws_iam_role.eks_node_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
}

resource "aws_iam_role_policy_attachment" "eks_registry_policy" {
  role       = aws_iam_role.eks_node_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}


# Output the repository URL
output "ecr_repository_url" {
  value = aws_ecr_repository.api.repository_url
}

# Output the cluster endpoint
output "eks_cluster_endpoint" {
  value = aws_eks_cluster.fastapi_cluster.endpoint
}
