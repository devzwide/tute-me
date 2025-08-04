#!/bin/bash
# Navigate to the application directory
cd /home/ec2-user/tute-me

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the Python dependencies from requirements.txt
pip install -r requirements.txt
