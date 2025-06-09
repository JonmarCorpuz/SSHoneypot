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

    #
    run_cmd('sudo su - cowrie -c "git clone http://github.com/cowrie/cowrie && cd cowrie && python3 -m venv cowrie-env && source cowrie-env/bin/activate && python -m pip install --upgrade pip && python -m pip install --upgrade -r requirements.txt && python -m pip install --upgrade -r requirements-output.txt && bin/cowrie start"')

    #
    run_cmd('sudo su - cowrie -c "cd cowrie && sed -i "/^\[telnet\]/,/^\[/{s/enabled *= *false/enabled = true/}" etc/cowrie.cfg.dist"')

def cron_job():

    #
    run_cmd('loginAttempts_filepath=$(sudo find / -type f -name "loginAttempts.sh" 2>/dev/null | head -n 1)')

    #
    run_cmd('sudo apt -y install cron')
    run_cmd('( crontab -l 2>/dev/null; echo "* * * * * $loginAttempts_filepath" ) | crontab -')

def main():

    install_cowrie()

    cron_job()

# ==== MAIN BODY ========================================================
if __name__ == "__main__":
    main()
