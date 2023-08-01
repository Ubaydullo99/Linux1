             ### SNPE sdk installation
# isntall snpe sdk here the link - https://qpm.qualcomm.com/#/main/tools/details/qualcomm_neural_processing_sdk
cd /opt/qcom/aistack/snpe/2.12.0.230626
ls

# below link solution for issue of qpm3 login
# https://developer.qualcomm.com/forum/qdn-forums/software/hexagon-dsp-sdk/toolsinstallation/70818


# setup sdk environment and dependencies
cd /opt/qcom/aistack/snpe/2.12.0.230626/bin
sudo apt update
sudo apt install python3-pip
check-linux-dependency.sh
check-python-dependency
# if errors encounters (python setup.py), fariler error code 1 in MarkupSafe
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install MarkupSafe
pip3 install mako==1.1.0
sudo pip3 install MarkupSafe
sudo pip3 install mako==1.1.0
check-python-dependency


# To check snpe working fine 
cd /opt/qcom/aistack/snpe/2.12.0.230626/bin
pip3 install tensorflow
./envcheck -t


# To use the snpe
uname -m
cd /opt/qcom/aistack/snpe/2.12.0.230626/bin/x86_64-linux-clang
./snpe-net-run
# issue Add the directory containing libSNPE.so to the LD_LIBRARY_PATH environment variable
sudo find / -name "libSNPE.so" 2>/dev/null
export LD_LIBRARY_PATH=/opt/qcom/aistack/snpe/2.12.0.230626/lib/x86_64-linux-clang:$LD_LIBRARY_PATH 
# issue - ./snpe-net-run: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found 

