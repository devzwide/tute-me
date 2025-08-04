#!/bin/bash
# Navigate to the application directory
cd /home/ec2-user/tute-me

# Activate the virtual environment
source venv/bin/activate

# Start the Flask application using Gunicorn on port 8000
# -w flag specifies the number of worker processes
# -b flag specifies the binding address and port
# `app:app` is the format for `[module_name]:[flask_app_instance_name]`
gunicorn --workers 3 --bind 0.0.0.0:8000 app:app &
