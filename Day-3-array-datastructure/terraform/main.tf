variable "instance_count" {
  default = 3
}

resource "aws_instance" "web" {
  count = var.instance_count
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "WebServer${count.index}"
  }
}


variable "allowed_ports" {
  default = [22, 80, 443]
}

resource "aws_security_group" "example" {
  name        = "example-sg"

  ingress {
    from_port   = var.allowed_ports[0]
    to_port     = var.allowed_ports[0]
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = var.allowed_ports[1]
    to_port     = var.allowed_ports[1]
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = var.allowed_ports[2]
    to_port     = var.allowed_ports[2]
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
