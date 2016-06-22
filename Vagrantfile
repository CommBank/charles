# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder ".", "/home/vagrant/host/"
  config.vm.network "private_network", ip: "192.168.50.4"

  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y build-essential python3-dev python3-pip python-pip python-dev libpng-dev libfreetype6-dev libxft-dev cython cython3
      sudo pip3 install virtualenv
      sudo pip install virtualenv
      mkdir /home/vagrant/workspace/
      chown vagrant /home/vagrant/workspace/
      cd /home/vagrant/workspace/
      virtualenv -p /usr/bin/python3 --system-site-packages venv
      source venv/bin/activate
      pip3 install jupyter numpy scipy matplotlib pandas sympy nose2
      export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0rc0-cp34-cp34m-linux_x86_64.whl
      sudo pip3 install --upgrade $TF_BINARY_URL
      echo "alias hydrokernel='ipython kernel --ip=192.168.50.4'" >> ~/.profile
      deactivate
  SHELL
end
