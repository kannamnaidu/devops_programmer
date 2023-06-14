provider "aws" {
  region = var.region
}

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.1.0"
    }
  }
}
---
variable "iam_user" {
    type = string
    default = "s3_user"
}

variable "iam_group" {
    type = string
    default = "s3_group"
}

variable "region" {
    type = string
    default = "us-east-1"
}
