#!/bin/bash

apt-get install -y git
apt-get install -y python3 python3-pip
pip3 install nltk
python3 -c "import nltk; nltk.download('punkt')"
pip3 install textgenrnn


git clone https://github.com/charlesreid1/joyce-tools.git /joyce-tools
chmod -R charlesreid1:charlesreid1 /joyce-tools

