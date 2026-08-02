# ☁️ SAIC Cloud Automation Toolkit (`saic-cloud-toolkit`)

**Classification:** `UNCLASSIFIED // INTERNAL USE ONLY`  
**Maintainer:** SAIC Cloud Architecture Practice (`cloud-architecture@saic.com`)

Enterprise-grade infrastructure-as-code (IaC) templates and Terraform modules for federal civilian and defense workloads.

## 🛠️ Repository Contents
* `main.tf`: Production Terraform HCL for GCP KMS keyrings (`saic-proposal-keyring`) and symmetric CMEK keys (`saic-cmek-v1`).
* `variables.tf`: Module input variables and defaults.
* `deploy_infrastructure.py`: Python automation script for IaC deployment.
* `architecture.md`: Multi-region architecture specifications (FIPS 140-3 HSM).
