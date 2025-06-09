#!/usr/bin/env python3

# ==== MODULES ==========================================================

# Provides functions for interacting with the operating system
import os
# Allows you to run shell commands and interact with system processes
import subprocess 
# Provides access to system-specific parameters and functions
import sys        

# ==== FUNCTIONS ========================================================

# Run a shell command (Exit if the command fails)
def run_cmd(cmd):

    # Run the command passed as the argument
    print(f'Running: {cmd}')
    result = subprocess.run(cmd, shell=True)

    # Exit if the command fails
    if result.returncode != 0:
        print(f'Command failed: {cmd}')
        sys.exit(1)

# Function to install and configure the cowrie honeypot
def cowrie():

    # Install system dependencies
    run_cmd('sudo apt-get -y install git python3-pip python3-venv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind &> /dev/null')

    # Add a dedicated cowrie user without a password (for sandboxing the honeypot) 
    run_cmd('sudo adduser --disabled-password --gecos "" cowrie')

    # Clone the Cowrie repository, set up Python virtual environment, install dependencies, and start Cowrie as the cowrie user
    run_cmd('sudo su - cowrie -c "git clone http://github.com/cowrie/cowrie && cd cowrie && python3 -m venv cowrie-env && source cowrie-env/bin/activate && python -m pip install --upgrade pip && python -m pip install --upgrade -r requirements.txt && python -m pip install --upgrade -r requirements-output.txt && bin/cowrie start"')

    # Enable the Telnet honeypot in Cowrie's default configuration file
    run_cmd('sudo su - cowrie -c "cd cowrie && sed -i "/^\[telnet\]/,/^\[/{s/enabled *= *false/enabled = true/}" etc/cowrie.cfg.dist"')

def elk_stack():

    # Install Elasticsearch
    run_cmd(' ')

    # Install Logstash
    run_cmd(' ')

    # Install Kibana
    run_cmd(' ')

def main():

    # Install and configure Cowrie
    cowrie()

    # Install and configure an ELK Stack
    elk_stack()

# ==== MAIN BODY ========================================================
if __name__ == "__main__":
    main()
