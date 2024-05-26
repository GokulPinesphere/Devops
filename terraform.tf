provider "aws"{
  region = "us-east-1"
}
resource "aws_instance" "my_instance"{
  ami = "AMI-12232322"
  resourse_type = "t2.micro"
  tags = {
    Name = "Instance"
  }
}
output "instance_ip" {
  value = my_instance_ip
}
