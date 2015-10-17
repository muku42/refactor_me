#!/usr/bin/env python
# COMMAND LINE PROGRAM TO DOWNLOAD A USER'S AVATAR FROM GITHUB.
# USAGE: `PYTHON get_avatar.py <GITHUB_USERNAME>`.

import sys
import json
import argparse
import requests
import shutil

# PARSE COMMAND LINE ARGUMENTS
parser = argparse.ArgumentParser()
parser.add_argument('username')
args = parser.parse_args()
# CALL THE GITHUB API AND GET USER INFO
requestURL = 'https://api.github.com/users/' + args.username
result = requests.get(requestURL)
if result.ok :
    user_info = json.loads(result.content)
    avatarURL = user_info['avatar_url']
else:
    sys.stderr.write("Error fetching user information for {0};\
                     exiting now, sorry...\n".format(args.username))
    sys.exit()
# DOWNLOAD AND SAVE IMAGE FILE
imageFile = requests.get(avatarURL, stream=True)
if imageFile.ok:
    with open(args.username + '.png', 'wb') as outFile:
        shutil.copyfileobj(imageFile.raw, outFile)
