# Configure the AWS provider
provider "aws" {
  region = "us-west-2"
}

# Create a VPC for the spacecraft's infrastructure
resource "aws_vpc" "spacecraft_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "Spacecraft VPC"
  }
}

# Create a subnet for the spacecraft's systems
resource "aws_subnet" "spacecraft_subnet" {
  cidr_block = "10.0.1.0/24"
  vpc_id     = aws_vpc.spacecraft_vpc.id
  availability_zone = "us-west-2a"
  tags = {
    Name = "Spacecraft Subnet"
  }
}

# Create an EC2 instance for the spacecraft's propulsion system
resource "aws_instance" "propulsion_instance" {
  ami           = "ami-abc123"
  instance_type = "c5.xlarge"
  vpc_security_group_ids = [aws_security_group.propulsion_sg.id]
  subnet_id = aws_subnet.spacecraft_subnet.id
  key_name               = "spacecraft_key"
  tags = {
    Name = "Propulsion Instance"
  }
}

# Create a security group for the spacecraft's propulsion system
resource "aws_security_group" "propulsion_sg" {
  name        = "propulsion_sg"
  description = "Security group for propulsion system"
  vpc_id      = aws_vpc.spacecraft_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
