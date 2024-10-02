variable "aws_access_key" {
  description = "AWS Access Key"
  type        = string
  default     = "" # Optional, but useful to avoid prompts

}

variable "aws_secret_key" {
  description = "AWS Secret Key"
  type        = string
  default     = "" # Optional, but useful to avoid prompts

}

variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "sa-east-1" # Change this to your desired default region
}
