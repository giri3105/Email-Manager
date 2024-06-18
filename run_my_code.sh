#!/bin/bash
# run_my_codes.sh

# First code
echo "Running first code..."
/home/giri/Email-project/read_emails.py
# Check if the first code ran successfully
if [ $? -eq 0 ]; then
  # Second code
  echo "Running second code..."
  /home/giri/Email-project/send_email.py
else
  echo "First code failed. Not running second code."
fi
