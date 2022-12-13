To run:
Clone project into a directory
https://github.com/csidon/AzAnonMontygo.git

#If pip is not already in your system
sudo apt-get install python-pip
# Note- You might need to install python3-pip instead

# Change directory to AzAnonMontygo
cd AzAnonMontygo

# Then install venv
pip install virtualenv
sudo pip3 install virtualenv

# check your installation
virtualenv --version

# Create a virtual environment
virtualenv venv
sudo 
# Use this article if you're running into venv installation issues
https://techoverflow.net/2022/02/03/how-to-fix-tox-attributeerror-module-virtualenv-create-via_global_ref-builtin-cpython-mac_os-has-no-attribute-cpython2macosarmframework/

# Activate the virtual environment
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt 
pip3 install -r requirements.txt 

# Run the program (on localhost)
python runner.py

# Run the program (on VM, ubuntu/nginx)
export FLASK_APP=runner.py
flask run -h 0.0.0.0