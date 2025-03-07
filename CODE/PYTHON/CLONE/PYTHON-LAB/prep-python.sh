#!/bin/bash

# Function to check if a package is installed
is_installed() {
    dpkg -l | grep -q "$1"
}

# Update system packages
sudo apt update

# Install required dependencies if not already installed
dependencies=(
    build-essential
    zlib1g-dev
    libncurses5-dev
    libgdbm-dev
    libnss3-dev
    libssl-dev
    libsqlite3-dev
    libreadline-dev
    libffi-dev
    curl
    libbz2-dev
)

for package in "${dependencies[@]}"; do
    if ! is_installed "$package"; then
        echo "Installing $package..."
        sudo apt install "$package" -y
    else
        echo "$package is already installed."
    fi
done

# Get the latest version of Python 3.9
PYTHON_VERSION=$(curl -s https://www.python.org/downloads/ | grep -o 'Python 3.9.[0-9]*' | head -n 1 | awk '{print $2}')

# Check if Python 3.9 is already installed
if ! command -v python3.9 &> /dev/null; then
    # Download Python 3.9 source code
    echo "Downloading Python $PYTHON_VERSION..."
    curl -O https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz

    # Extract the source code
    tar -xf Python-$PYTHON_VERSION.tgz

    # Navigate to the extracted directory
    cd Python-$PYTHON_VERSION || exit

    # Configure and build Python
    ./configure --enable-optimizations
    make -j "$(nproc)"

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
    cd .. || exit
    rm -rf Python-$PYTHON_VERSION Python-$PYTHON_VERSION.tgz

    echo "Python $PYTHON_VERSION, pip, and pip3 have been updated successfully and set as default!"
else
    echo "Python 3.9 is already installed."
fi

# Install Git Clone if not already installed
if ! is_installed "git"; then
    echo "Installing Git..."
    sudo apt-get install git -y
else
    echo "Git is already installed."
fi

# Install GitHub Clone if not already installed
if ! pip show github-clone &> /dev/null; then
    echo "Installing GitHub Clone..."
    sudo pip install github-clone
else
    echo "GitHub Clone is already installed."
fi

# Setting Permissions
sudo chmod -R 777 /root/

# Install Nano if not already installed
if ! is_installed "nano"; then
    echo "Installing Nano..."
    sudo apt-get install nano -y
else
    echo "Nano is already installed."
fi

# Upgrade DNA Center SDK and other Dependencies
if [ -f requirements.txt ]; then
    echo "Upgrading dependencies from requirements.txt..."
    sudo pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation."
fi
