# To create environment in Ubuntu 18.04 in rb5 device
  
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

#### ref: https://www.linode.com/docs/guides/create-a-python-virtualenv-on-ubuntu-18-04/



```console
sudo apt install python3-venv
python3 -m venv argosrb
source argosrb/bin/activate
python
pip install numpy
deactivate
```

### for activating venv and deactivate
```console
source argosrb/bin/activate
deactivate
```

### for check the package version rather than --version
```console
import numpy as np
print(np.__version__)
```
- or
```console
python -c "import numpy as np; print(np.__version__)"
```   


## To create venv with python level for Ubuntu 20.04 for VM
    sudo apt update

    # install venv tools
    sudo apt install python3.8 python3.8-venv

    python3.8 -m venv myenv
    source myenv/bin/activate
