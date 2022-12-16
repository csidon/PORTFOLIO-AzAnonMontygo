#################################################################
#    Instructions to install AzAnonymous
#================================================================
# This assumes you already have Nginx installed on your Ubuntu VM
# with your MongoDB hosted on CosmosDB
#-----------------------------------------------------------------
# Tech stack: 
# Ubuntu 20.04.5 LTS and above
# MongoDB (hosted on Azure CosmosDB)
# Python3 (python3-pip, pymongo, python-dotenv)
# Flask
# Gunicorn


# Clone project into a directory
git clone https://github.com/csidon/AzAnonMontygo.git

#If pip is not already in your system
sudo apt-get install python3-pip instead

# Change directory to AzAnonMontygo
cd AzAnonMontygo

#=================================================================
#    Development server deployment instructions
#-----------------------------------------------------------------

# Install venv
sudo pip3 install virtualenv
pip install virtualenv (windows local test)


# Check your installation
virtualenv --version

# Create a virtual environment
virtualenv venv

# Use this article if you're running into venv installation issues
https://techoverflow.net/2022/02/03/how-to-fix-tox-attributeerror-module-virtualenv-create-via_global_ref-builtin-cpython-mac_os-has-no-attribute-cpython2macosarmframework/

# Activate the virtual environment
source venv/bin/activate
venv\Scripts\activate.bat (on localhost Windows)

# Install the requirements
pip3 install -r requirements.txt 
pip install -r requirements.txt 

# Run the program (on localhost)
python runner.py

# Run the program (on VM, ubuntu/nginx)
export FLASK_APP=runner.py
flask run -h 0.0.0.0

#=================================================================
#    Development server deployment instructions
#-----------------------------------------------------------------
# First we need to make sure that Nginx is configured to listen to port 80 and redirect traffic to port 8000 (which gunicorn uses).

# Move the nginx config file to the sites-enabled folder
sudo mv AzAnonMontygo/flask_azanon_app /etc/nginx/sites-enabled/

# Break the link between the default nginx config
sudo unlink /etc/nginx/sites-enabled/default

# Test the nginx file syntax
sudo nginx -t

# Restart Nginx so that the system will pick up the new conf file
sudo systemctl restart nginx

# Make sure you're in the AzAnonMontygo directory, then run app
gunicorn --workers=3 runner:app

# Open <<VMIPaddress>> in browser and check if it's working 
# If working, add a flag that allows the app to run in the background
gunicorn --workers=3 runner:app --daemon
