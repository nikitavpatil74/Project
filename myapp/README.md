# MyApplication - FastAPI Service

## Description
Lightweight FastAPI application serving an `/info` endpoint and `/ui` page, dockerized and deployable via Helm on AKS.This project demonstrates a containerized FastAPI microservice, deployed on a Kubernetes cluster using Helm for configuration and management. It is designed to be cloud-ready, scalable, and easy to deploy in various environments (local or cloud providers like Azure, GCP, AWS).

## Features
REST API Endpoint: /info

HTML UI Endpoint: /ui

Dockerized for portability

Deployed on Azure Kubernetes Service (AKS)

Infrastructure as Code with Terraform

Helm chart-based deployment

## Create and use a Python virtual environment (recommended):
Step 1: Create a virtual environment in your project folder
python3 -m venv venv
Step 2: Activate the virtual environment
source venv/bin/activate

## Install Dependencies
pip install -r requirements.txt

## Build with Docker
Create DockerFile
Step 1:Build Image
docker build -t myapp:latest .
Step 2:Run Locally
docker run -e GIT_COMMIT_SHA=abc123 -e SERVICE_PORT=8080 -e LOG_LEVEL=INFO -p 8081:8080 myapp:latest
Access App
•	JSON API: http:// 20.185.252.188:8081/info
•	Web UI: http:// 20.185.252.188:8081/ui

![Screenshot 2025-06-09 060423](https://github.com/user-attachments/assets/9f40c7f5-7f08-485f-af3b-a10f953a3e16)
![Screenshot 2025-06-09 060758](https://github.com/user-attachments/assets/7052fead-9650-4fa2-8fd2-512a0fd46be4)
![Screenshot 2025-06-09 060837](https://github.com/user-attachments/assets/55674fa8-f01d-4538-a47b-e2f64b0a12de)


## On Microsoft Azure create Resource group
Step 1: 1.	In the Azure portal, click "Create a resource".
        2.	Search for Resource Group → Click Create.
        3.	Fill the form:
	          Name: fastapi-rg 
            Region: Select your region (East US)
        4.	Click Review + Create, then Create.
Step 2:Create Azure Kubernetes Service (AKS)
        1. Go to Kuberenetes Service
        2. Create Kubernetes Cluster
<img width="950" alt="image" src="https://github.com/user-attachments/assets/97939f21-23b1-49e9-ab41-6c9bd56fccc4" />


## Connect To AKS
Step 1: az login
Step 2: az aks get-credentials --resource-group (name)--name fastapi-cluster --overwrite-existing

## Push Docker image to Azure Container Registry
Step 1: Create ACR
az acr create --resource-group (name) --name (registryname) --sku Basic
az acr login --name (registryname)
Step 2: Tag and Push image
docker tag myapp:latest (registryname).azurecr.io/myapp:latest
docker push (registryname).azurecr.io/myapp:latest

## Kubernetes Deployment using Kubectl
Step 1: Create deployment.yaml file
Step 2: kubectl apply -f deployment.yaml
Step 3: kubectl get pods -w
Step 4: kubectl get service 
Access App
•	JSON API: http:// External-ip/info
•	Web UI: http:// External-ip/ui

## Infrastructure as code with Terraform
Step 1: Create main.tf file
Step 2: Initialize & Apply Terraform
terraform init
terraform plan
terraform apply

## Helm Deployment
Step 1: Create Chart.yaml and values.yaml
Step 2: Create templates folder and create deployment.yaml, service.yaml and secret.yaml files
Step 3: helm lint .
Step 4: helm install myapp-release .
Step 5: kubectl get pods -w
Step 6: kubectl get svc
Access App
•	JSON API: http:// External-ip/info
•	Web UI: http:// External-ip/ui

## Tech Stack
Backend: Python, FastAPI

Templates: Jinja2

Containerization: Docker

Cloud: Microsoft Azure (AKS + ACR)

IaC: Terraform

Orchestration: Kubernetes

Package Management: Helm







