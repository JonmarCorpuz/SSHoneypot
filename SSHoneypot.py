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

def main():

    run_cmd('mkdir -p logstash/pipeline && sudo mv pipeline.conf ./logstash/pipeline.conf')
    run_cmd('mkdir filebeat && sudo mv filebeat.yaml ./filebeat/filebeat.yaml')

    run_cmd('sudo apt -y install docker docker-compose &> /dev/null')
    
    run_cmd('sudo docker-compose up -d')

# ==== MAIN BODY ========================================================
if __name__ == "__main__":
    main()
