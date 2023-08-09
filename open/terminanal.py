wsl --list --online  # check available linux env for windows
wsl --install -d Ubuntu-18.04 #isntalling ubuntu on windows

wsl ~ -u root # enter to root
# https://learn.microsoft.com/en-us/windows/wsl/install

sudo su # to access the root 



                                    ### Tensorflow installation
# https://developer.qualcomm.com/sites/default/files/docs/snpe/setup_tensorflow.html 
sudo apt update
sudo apt install python3-pip
sudo pip3 install tensorflow

### Python version update
sudo apt install python3.7
sudo apt install python3.7-distutils
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
python3 --version
sudo pip3 install tensorflow

# checking numpy versoin with python3 method instead of numpy --version.
pip3 install Cython
pip3 install numpy
pip3 install h5py
python3 -c "import numpy; print(numpy.__version__)"
python3 -c "import h5py; print(h5py.__version__)"
pip3 install tensorflow
python3 -c "import tensorflow as tf; print(tf.__version__)"

