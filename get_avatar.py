#!/usr/bin/env python

# This is a command line program to download a user's avatar from
# GitHub.  Usage: 'python get_avatar.py <GitHub_username>

import sys
import json
import argparse
import requests
import shutil

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('username')
args = parser.parse_args()

# Call the GitHub api and get user info
requestURL = 'https://api.github.com/users/' + args.username
result = requests.get(requestURL)
if result.ok :
    user_info = json.loads(result.content)
    avatarURL = user_info['avatar_url']
else:
    sys.stderr.write("Error fetching user information for {0};\
                     exiting now, sorry...\n".format(args.username))
    sys.exit()

# Download and save image file
imageFile = requests.get(avatarURL, stream=True)
if imageFile.ok:
    with open(args.username + '.png', 'wb') as outFile:
        shutil.copyfileobj(imageFile.raw, outFile)
