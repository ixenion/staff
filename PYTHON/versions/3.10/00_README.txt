# INSTALLATION

video:
https://www.youtube.com/watch?v=7H-DcdSmV0U&ab_channel=KamrulsKode

1. For compiling the source code install essential packages. (If you havent done this before)
sudo apt install wget build-essential checkinstall
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

2. Download Python 3.10 source code from the official download site in the Desktop.
sudo wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz

3. Extract the downloaded archive file and prepare the source for the installation.
tar xzf Python-3.10.4.tgz
cd Python-3.10.4
sudo ./configure --enable-optimizations

4. Now, install Python 3.10 on your system.
sudo make altinstall

5. Verify the installed version:
python3.10 --version



# CHANGELOG TUTORIAL
# https://youtu.be/0kyy_zKO86U

# in shor

1. better type hinting
2. better traceback
3. pattern matching	(match|case)
