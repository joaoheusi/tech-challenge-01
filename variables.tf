variable "aws_access_key" {
  description = "AWS Access Key"
  type        = string
  default     = ""  # Leave empty; will be populated via environment variables
}

variable "aws_secret_key" {
  description = "AWS Secret Key"
  type        = string
  default     = ""  # Leave empty; will be populated via environment variables
}

variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "sa-east-1"
}
