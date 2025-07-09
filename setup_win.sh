#!/bin/bash

wget "https://files.pythonhosted.org/packages/3c/e3/e868f1d5951047f950d2ba1e04a765a3328a51f06996b67976d6102f8227/tensorflow-2.19.0-cp311-cp311-win_amd64.whl"
pip install tensorflow-2.19.0-cp311-cp311-win_amd64.whl
pip install -r requirements.txt

echo "DONE"