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

def install_cowrie():
    print("")

def install_elasticsearch():
    print("")

def install_kibana():
    print("")

# ==== MAIN BODY ========================================================
if __name__ == "__main__":
    main()
