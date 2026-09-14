variable "project_name" {
  type = string
}

variable "environment" {
  type = string
}

variable "public_subnet_ids" {
  type = list(string)
}

variable "app_security_group_id" {
  type = string
}

variable "target_group_arn" {
  type = string
}

variable "db_host" {
  type = string
}

variable "db_port" {
  type = number
}

variable "db_name" {
  type    = string
  default = "support_desk"
}

variable "db_username" {
  type    = string
  default = "support_desk"
}

variable "db_password" {
  type      = string
  sensitive = true
}

variable "container_image" {
  type    = string
  default = "vinsl/support-desk:1.0.1"
}