output "load_balancer_dns_name" {
  value = module.load_balancer.dns_name
}

variable "db_password" {
  description = "Database master password. Supply through TF_VAR_db_password."
  type        = string
  sensitive   = true
}

output "rds_endpoint" {
  value = module.database.endpoint
}