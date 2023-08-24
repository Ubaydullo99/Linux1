# to change onnx file to dlc file format
    cd x86_64-linux-clang

    # missing packages
    pip install packaging
    export PYTHONPATH=$PYTHONPATH:/opt/qcom/aistack/snpe/2.13.0.230730/lib/python
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/qcom/aistack/snpe/2.13.0.230730/lib/x86_64-linux-clang
    pip install PyYAML
    pip install onnx

    ./snpe-onnx-to-dlc -i ~/Downloads/best.onnx -o ~/Downloads/best.dlc
