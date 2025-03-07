#!/bin/bash

# Function to check if a package is installed
is_installed() {
    dpkg -l | grep -q "$1"
}

# Function to remove a package if installed
remove_package() {
    if is_installed "$1"; then
        echo "Removing $1..."
        sudo apt-get remove --purge "$1" -y
    fi
}

# Function to check installed Python package version
check_python_package_version() {
    installed_version=$(python3.9 -m pip show "$1" | grep Version | awk '{print $2}')
    echo "$installed_version"
}

# Update the package list
echo "Updating package list..."
sudo apt update

# List of required system packages
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
    python3-apt
)

# Remove and install required system packages
for package in "${dependencies[@]}"; do
    remove_package "$package"
    echo "Installing $package..."
    sudo apt install "$package" -y
done

# Check if Python 3.9 is installed
if ! command -v python3.9 &> /dev/null; then
    echo "Python 3.9 is not installed. Please install it manually."
    exit 1
fi

# Remove existing pip installations
remove_package "python3-pip"

# Install pip using get-pip.py
echo "Installing pip..."
curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.9 get-pip.py

# Upgrade pip and setuptools
echo "Upgrading pip and setuptools..."
sudo python3.9 -m pip install --upgrade pip setuptools --no-cache-dir

# List of required Python packages
required_packages=(
    dnacentersdk==2.6.10
    PyGithub==2.1.1
    python-dotenv==1.0.0
    PyYAML==6.0.1
    requests==2.28.2
    urllib3==1.26.14
)

# Check the installed version of dnacentersdk
dnacentersdk_version=$(check_python_package_version "dnacentersdk")

if [[ "$dnacentersdk_version" != "2.6.10" ]]; then
    # Remove dnacentersdk if the version is not 2.6.10
    echo "Removing dnacentersdk version $dnacentersdk_version..."
    sudo python3.9 -m pip uninstall dnacentersdk -y
    echo "Installing dnacentersdk version 2.6.10..."
    sudo python3.9 -m pip install dnacentersdk==2.6.10 --no-cache-dir
else
    echo "dnacentersdk version 2.6.10 is already installed."
fi

# Remove and install other required Python packages
for pkg in "${required_packages[@]}"; do
    package_name=$(echo "$pkg" | cut -d'=' -f1)
    if [[ "$package_name" != "dnacentersdk" ]]; then
        remove_package "$package_name"
        echo "Installing $pkg..."
        sudo python3.9 -m pip install "$pkg" --no-cache-dir
    fi
done

# Check for requirements.txt and install if it exists
if [ -f requirements.txt ]; then
    echo "Installing dependencies from requirements.txt..."
    sudo python3.9 -m pip install -r requirements.txt --no-cache-dir
else
    echo "requirements.txt not found. Skipping dependency installation."
fi

# Check for any pip conflicts
echo "Checking for pip conflicts..."
pip check

echo "Setup complete. All packages have been installed globally."
