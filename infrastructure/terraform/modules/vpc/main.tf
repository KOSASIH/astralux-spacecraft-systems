# VPC module for the spacecraft's infrastructure
resource "aws_vpc" "spacecraft_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "spacecraft_subnet" {
  cidr_block = "10.0.1.0/24"
  vpc_id     = aws_vpc.spacecraft_vpc.id
  availability_zone = "us-west-2a"
}
