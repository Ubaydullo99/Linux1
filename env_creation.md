# To create environemtn in Ubuntu 18.04

```console
sudo apt-get update
sudo apt-get upgrade

sudo apt install virtualenv
mkdir ~/python-environments
cd ~/python-environments
virtualenv --python=/usr/bin/python3.6 envname
ls
cd envname
ls
source bin/activate   # activate environment

```
