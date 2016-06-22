#! /bin/bash

ssh -F vagrant-ssh default "cd /home/vagrant/workspace/ ; source venv/bin/activate ; ipython3 kernel --ip='192.168.50.4' -f /tmp/kernel.json"
