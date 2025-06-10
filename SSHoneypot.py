#!/usr/bin/env python3

# ==== MODULES ==========================================================
import os
import subprocess 
import sys        

# ==== FUNCTIONS ========================================================
def run_cmd(cmd):

    # Run the command passed as the argument
    print(f'Running: {cmd}')
    result = subprocess.run(cmd, shell=True)

    # Exit if the command fails
    if result.returncode != 0:
        print(f'Command failed: {cmd}')
        sys.exit(1)

def cowrie():

    # Install system dependencies
    run_cmd('sudo apt -y update')
    run_cmd('sudo apt-get -y install git python3-pip python3-venv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind &> /dev/null')

    # Add a dedicated cowrie user without a password (for sandboxing the honeypot) 
    run_cmd('sudo adduser --disabled-password --gecos "" cowrie')

    # Clone the Cowrie repository, set up Python virtual environment, install dependencies, and start Cowrie as the cowrie user
    run_cmd('sudo su - cowrie -c "git clone http://github.com/cowrie/cowrie && cd cowrie && python3 -m venv cowrie-env && source cowrie-env/bin/activate && python -m pip install --upgrade pip && python -m pip install --upgrade -r requirements.txt && python -m pip install --upgrade -r requirements-output.txt && bin/cowrie start"')

    # Enable the Telnet honeypot in Cowrie's default configuration file
    #run_cmd('sudo su - cowrie -c "cd cowrie && sed -i "/^\[telnet\]/,/^\[/{s/enabled *= *false/enabled = true/}" etc/cowrie.cfg.dist"')

def elk_stack():

    # Install Elasticsearch
    run_cmd('curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic.gpg')
    run_cmd('echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list')
    run_cmd('sudo apt -y update')
    run_cmd('sudo apt -y install elasticsearch')
    run_cmd('sudo sed -i "s/^#\s*\(network\.host:\s*localhost\)/\1/" /etc/elasticsearch/elasticsearch.yml')
    run_cmd('sudo systemctl start elasticsearch')
    run_cmd('sudo systemctl enable elasticsearch')

    # Install Logstash
    run_cmd('wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg')
    run_cmd('sudo apt-get -y install apt-transport-https')
    run_cmd('echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-9.x.list')
    run_cmd('sudo apt-get -y update && sudo apt-get -y install logstash')

    # Install Kibana
    run_cmd('wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg')
    run_cmd('sudo apt-get -y install apt-transport-https')
    run_cmd('echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list')
    run_cmd('sudo apt-get -y update && sudo apt-get -y install kibana')
    run_cmd('sudo sed -i "s/^#\s*server\.host:\s*localhost/server.host: 0.0.0.0/" /etc/kibana/kibana.yml')
    run_cmd('sudo /bin/systemctl daemon-reload')
    run_cmd('sudo /bin/systemctl enable kibana.service')
    run_cmd('sudo systemctl start kibana.service')

def main():

    # Install and configure Cowrie
    cowrie()

    # Install and configure an ELK Stack
    elk_stack()

# ==== MAIN BODY ========================================================
if __name__ == "__main__":
    main()
