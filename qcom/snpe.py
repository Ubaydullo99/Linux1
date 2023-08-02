             ### SNPE sdk installation
# isntall snpe sdk here the link - https://qpm.qualcomm.com/#/main/tools/details/qualcomm_neural_processing_sdk
#https://developer.qualcomm.com/software/qualcomm-neural-processing-sdk/windows-on-snapdragon

sudo dpkg -i QualcommPackageManager3.3.0.83.1.Linux-x86.deb
sudo apt-get install -f
qpm --version
qpm-cli --login
qpm-cli --license-activate qualcomm_neural_processing_sdk
qpm-cli --extract qualcomm_neural_processing_sdk # (or)
qpm-cli --extract <full path to downloaded .qik file>

cd /opt/qcom/aistack/snpe/2.12.0.230626
ls

# below link solution for issue of qpm3 login
# https://developer.qualcomm.com/forum/qdn-forums/software/hexagon-dsp-sdk/toolsinstallation/70818


# setup sdk environment and dependencies
cd /opt/qcom/aistack/snpe/2.12.0.230626/bin
sudo apt update
sudo apt install python3-pip
./check-linux-dependency.sh
# or
export PATH="$PATH:/opt/qcom/aistack/snpe/2.13.0.230730/bin" # set full path to script
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

























# ref
# Run snpe-sample with the Alexnet model on the target. This assumes that you have done the setup steps for running Run on Android Target to push to the target all the sample data files and Alexnet model.

adb shell
export SNPE_TARGET_ARCH=arm-android-clang6.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/local/tmp/snpeexample/$SNPE_TARGET_ARCH/lib
export PATH=$PATH:/data/local/tmp/snpeexample/$SNPE_TARGET_ARCH/bin
cd /data/local/tmp/alexnet
snpe-sample -b ITENSOR -d bvlc_alexnet.dlc -i target_raw_list.txt -o output_sample
exit
