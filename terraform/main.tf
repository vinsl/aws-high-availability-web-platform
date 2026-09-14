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