variable "project_name" {
  type = string
}

variable "environment" {
  type = string
}

variable "private_subnet_ids" {
  type = list(string)
}

variable "database_security_group_id" {
  type = string
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
  description = "Database master password."
  type        = string
  sensitive   = true
}