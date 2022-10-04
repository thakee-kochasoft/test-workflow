
terraform {
  required_providers {
    ibm = {
      source  = "IBM-Cloud/ibm"
      version = ">= 1.12.0"
    }
  }
}


variable "api_key" {}


provider "ibm" {
  ibmcloud_api_key = var.api_key
  region           = "us-east"
}


data "ibm_is_image" "blackbox" {
   name = "blackbox"
}


output "image_id" {
  value = data.ibm_is_image.blackbox.id
}
