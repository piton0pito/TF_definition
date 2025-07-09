#!/bin/bash

wget "https://files.pythonhosted.org/packages/ba/1c/370b5546cf7afc29649b2fb74c171ef2493a36f62cf901c1425ead4a56af/tensorflow-2.19.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
pip install tensorflow-2.19.0-cp311-cp311-win_amd64.whl
pip install -r requirements.txt

echo "DONE"