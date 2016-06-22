#! /bin/bash

vagrant ssh-config > vagrant-ssh
ssh -F vagrant-ssh default cat /tmp/kernel.json > hydrogen/connection.json
