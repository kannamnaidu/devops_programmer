resource "aws_vpc" "my_vpc" {
  cidr_block       = var.cidr_block
  instance_tenancy = "default"
  enable_dns_hostnames = true

  tags = {
    Name = var.vpc_name
  }
}

resource "aws_internet_gateway" "my_Igw" {
  vpc_id     = aws_vpc.my_vpc.id

  tags = {
    Name = var.internet_gateway_name
  }
}
