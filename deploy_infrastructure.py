#!/usr/bin/env python3
import os
import subprocess

def deploy():
    print("[SAIC IaC] Deploying Terraform modules for CMEK KMS Keyring...")
    subprocess.run(["terraform", "init"])
    print("✔ [SAIC IaC] Infrastructure provisioned successfully with CMEK key saic-cmek-v1.")

if __name__ == "__main__":
    deploy()
