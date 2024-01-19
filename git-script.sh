#!/bin/bash

USER_NAME="hamza1100"
TOKEN="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"


# commands to create folder and file and add content to the file
# mkdir backend
# touch backend.py
# echo 'I am learning python Django along with AWS & Docker' > backend.py

# commands to stage, commit, and push the code the remote repository
git add .
git commit -m "dockerize app"

git push https://${USER_NAME}:${TOKEN}@github.com/${USER_NAME}/blog.git dockerize-app