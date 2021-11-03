#!/usr/bin/env bash

pip uninstall proces -y

python setup.py clean
python setup.py install
