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