terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }

  required_version = ">= 1.0"
}

provider "azurerm" {
  features {}
  subscription_id = "2aca5a48-1f02-4399-9c64-1700f5dd58e6"
}

# Resource Group
resource "azurerm_resource_group" "main" {
  name     = "fastapi-rg-tf"
  location = "East US"
}

# Storage Account
resource "azurerm_storage_account" "bucket" {
  name                     = "myappbucketdemo2025"  # must be globally unique
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  # Optional best practices
  #allow_blob_public_access = false
  min_tls_version          = "TLS1_2"
}

# Create a Blob Container (like a bucket)
resource "azurerm_storage_container" "appdata" {
  name                  = "myapp-data"
  storage_account_name  = azurerm_storage_account.bucket.name
  container_access_type = "private"
}
