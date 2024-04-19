cudnn_ver="8.9.4.*-1+cuda11.8"
apt update
apt upgrade -y
apt install software-properties-common wget curl python3-dev python3-pip python3-wheel python3-setuptools -y
python3 -m pip install --upgrade pip
pip3 install --user -r .devcontainer/requirements.txt
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
dpkg -i cuda-keyring_1.0-1_all.deb
rm cuda-keyring_1.0-1_all.deb
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /" -y
apt update
apt install libcudnn8=${cudnn_ver}
apt install libcudnn8-dev=${cudnn_ver}
apt install zlib1g g++ freeglut3-dev libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev libfreeimage-dev -y
pip3 cache purge
apt autoremove -y
apt clean
