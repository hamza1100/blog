#!/bin/bash

USER_NAME="your username"
TOKEN="your git personal access token"


# commands to create folder and file and add content to the file
# mkdir backend
# touch backend.py
# echo 'I am learning python Django along with AWS & Docker' > backend.py

# commands to stage, commit, and push the code the remote repository
git add .
git commit -m "commit message from git script"

git push https://${USER_NAME}:${TOKEN}@github.com/${USER_NAME}/blog.git dockerize-app
