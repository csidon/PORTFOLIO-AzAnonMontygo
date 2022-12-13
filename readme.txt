To run:
Clone project into a directory

#If pip is not already in your system
sudo apt-get install python-pip

# Then install venv
pip install virtualenv


# check your installation
virtualenv --version

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
venv\Scripts\activate   


# Install the requirements
pip install -r requirements.txt 

# Run the program
python runner.py