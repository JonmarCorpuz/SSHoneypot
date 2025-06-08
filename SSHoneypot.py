#!/usr/bin/env python3

# ==== MODULES ==========================================================
import os
import subprocess
import sys

# ==== VARIABLES ========================================================


# ==== FUNCTIONS ========================================================

# Run a shell command (Exit if the command fails)
def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

def verify_dependencies():
    try:
        run_cmd('sudo docker --version')

    except subprocess.CalledProcessError:
        run_cmd('sudo apt update')
        run_cmd('sudo apt install -y ca-certificates curl gnupg lsb-release')

        run_cmd('sudo mkdir -p /etc/apt/keyrings')
        run_cmd('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg')

        run_cmd('echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] '
                'https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | '
                'sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')

        run_cmd('sudo apt update')
        run_cmd('sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin')

        run_cmd('sudo systemctl start docker')
        run_cmd('sudo systemctl enable docker')

        run_cmd('sudo docker --version')

    def build_deployment():ls
    
        run_cmd('sudo docker-compose up -d')

# ==== MAIN BODY ========================================================
