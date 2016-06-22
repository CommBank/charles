# charles

A repo to capture my experiments with:

- tensorflow
- Numenta
- OpenBCI
- Python: Numpy, scipy, panda, matplotlib

## Getting started

1. Install Atom and the Atom package hydrogen (https://atom.io/packages/hydrogen)
2. Install Vagrant and VirtualBox
3. Clone this repo
4. ```vagrant up```
5. ```./start-kernel.sh```
6. ```./update-connection.sh```
7. Simply run hydrogen commands and these will execute against the Python3 Kernel in the VM

If you need to kill the kernel, you have do so from Hydrogen and then simply run ```./start-kernel.sh``` and ```./update-connection.sh``` again.

# Improvements

- Move these script hacks into a PR for the Hydrogen package 
