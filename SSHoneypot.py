#!/usr/bin/env python3

# ==== MODULES ==========================================================
import os
import subprocess
import sys

# ==== VARIABLES ========================================================


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

def install_cowrie():

    # Install system dependencies
    run_cmd('sudo apt-get -y install git python3-pip python3-venv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind &> /dev/null')

    # 
    run_cmd('sudo adduser --disabled-password --gecos "" cowrie')
    run_cmd('sudo su - cowrie')

    #
    run_cmd('git clone http://github.com/cowrie/cowrie && cd cowrie')

    #
    run_cmd('python3 -m venv cowrie-env')
    run_cmd('source cowrie-env/bin/activate')

    #
    run_cmd('python -m pip install --upgrade pip')
    run_cmd('python -m pip install --upgrade -r requirements.txt &> /dev/null')
    run_cmd('python -m pip install --upgrade -r requirements-output.txt &> /dev/null')

    #
    run_cmd('bin/cowrie start')

    #
    run_cmd('sed -i "/^\[telnet\]/,/^\[/{s/enabled *= *false/enabled = true/}" etc/cowrie.cfg.dist')


def install_elasticsearch():
    print("")

def install_kibana():
    print("")

def main():
    install_cowrie()

# ==== MAIN BODY ========================================================
if __name__ == "__main__":
    main()
