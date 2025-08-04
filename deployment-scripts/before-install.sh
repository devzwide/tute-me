#!/bin/bash
# Stop any existing Gunicorn process to prevent conflicts
# -f flag finds the process running from the specified path
# -9 flag forcefully kills the process
sudo pkill gunicorn || true
