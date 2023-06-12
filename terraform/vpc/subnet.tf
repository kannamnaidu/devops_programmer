resource "aws_subnet" "public_subnet" {
  count             = length(var.public_subnet_cidr)
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = element(var.public_subnet_cidr, count.index)
  availability_zone = element(var.azs, count.index)
  tags = {
    Name = "${var.vpc_name}-public_subnet-${count.index + 1}"
  }
