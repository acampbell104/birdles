#!/bin/bash

echo "🔧 Installing birdbath-ai..."

sudo apt update
sudo apt install -y python3-pip python3-venv git libjpeg-dev zlib1g-dev libatlas-base-dev libopenjp2-7-dev libtiff5

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

mkdir -p labelled captures logs models static templates
touch seen_today.json
echo '{}' > seen_today.json
