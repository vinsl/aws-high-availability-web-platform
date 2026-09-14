locals {
  project_name = "support-desk"
}

module "network" {
  source = "./modules/network"

  project_name = local.project_name
  environment  = var.environment
  vpc_cidr     = var.vpc_cidr
}

module "security" {
  source = "./modules/security"

  project_name = local.project_name
  environment  = var.environment
  vpc_id       = module.network.vpc_id
}

module "load_balancer" {
  source = "./modules/load_balancer"

  project_name          = local.project_name
  environment           = var.environment
  vpc_id                = module.network.vpc_id
  public_subnet_ids     = module.network.public_subnet_ids
  alb_security_group_id = module.security.alb_security_group_id
}


module "database" {
  source = "./modules/database"

  project_name               = local.project_name
  environment                = var.environment
  private_subnet_ids         = module.network.private_subnet_ids
  database_security_group_id = module.security.database_security_group_id
  db_password                = var.db_password
}

module "ecs" {
  source = "./modules/ecs"

  project_name = local.project_name
  environment  = var.environment

  public_subnet_ids     = module.network.public_subnet_ids
  app_security_group_id = module.security.app_security_group_id
  target_group_arn      = module.load_balancer.target_group_arn

  db_host     = module.database.endpoint
  db_port     = module.database.port
  db_password = var.db_password

  container_image = "vinsl/support-desk:1.0.1"
}