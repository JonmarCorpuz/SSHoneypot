#!/bin/bash

# ==== FAILED ATTEMPTS ==================================================

if ! file /home/$USER/cowrieLogins/failed.json;
then
  touch /home/$USER/cowrieLogins/failed.json
fi

sudo su -c 'cat /home/cowrie/cowrie/var/log/cowrie/cowrie.json' | grep "login.failed" > /home/$USER/cowrieLogins/failed.json

# ==== SUCCESSFUL ATTEMPTS ==============================================

if ! file /home/$USER/cowrieLogins/success.json;
then
  touch /home/$USER/cowrieLogins/success.json
fi

sudo su -c 'cat /home/cowrie/cowrie/var/log/cowrie/cowrie.json' | grep "login.success" > /home/$USER/cowrieLogins/success.json
