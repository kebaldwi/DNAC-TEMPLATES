#!/bin/bash

# Update Jenkins
sudo service jenkins stop
mv jenkins_date.tar.gz $HOME
cd /usr/share/jenkins
sudo mv jenkins.war jenkins.war.old
sudo wget https://updates.jenkins-ci.org/latest/jenkins.war
sudo chown root:root jenkins.war
sudo service jenkins start
cat /var/lib/jenkins/config.xml | grep '<version>'
sudo usermod -aG docker jenkins
sudo usermod -a -G root jenkins

# Update system packages
sudo apt update

# Install required dependencies
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev -y

# Get the latest version of Python 3.9
PYTHON_VERSION=$(curl -s https://www.python.org/downloads/ | grep -o 'Python 3.9.[0-9]*' | head -n 1 | awk '{print $2}')

# Download Python 3.9 source code
curl -O https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz

# Extract the source code
tar -xf Python-$PYTHON_VERSION.tgz

# Navigate to the extracted directory
cd Python-$PYTHON_VERSION

# Configure and build Python
./configure --enable-optimizations
make -j $(nproc)

# Install Python
sudo make altinstall

# Set Python 3.9 as the default version for python and python3 commands
sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python$PYTHON_VERSION 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python$PYTHON_VERSION 1

# Update pip and pip3
sudo python$PYTHON_VERSION -m ensurepip --upgrade
sudo python$PYTHON_VERSION -m pip install --upgrade pip
sudo python$PYTHON_VERSION -m pip install --upgrade setuptools wheel
sudo update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip$PYTHON_VERSION 1
sudo update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip$PYTHON_VERSION 1

# Cleanup
cd ..
rm -rf Python-$PYTHON_VERSION Python-$PYTHON_VERSION.tgz

echo "Python $PYTHON_VERSION, pip, and pip3 have been updated successfully and set as default!"

# Install Git Clone
sudo apt-get install gitclone
sudo pip install github-clone

# Clone the repo
ghclone https://github.com/kebaldwi/DEVWKS-2176

# Setting Permissions for Jenkins
sudo chmod -R 777 /root/

