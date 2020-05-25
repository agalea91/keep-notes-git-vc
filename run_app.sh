#!/bin/bash

cd /home/alex/keep-notes-git-vc

echo "Updating local filestore"
docker-compose up --build

echo "Updating remote filestore"
cd ~/Keep\ Notes\ Backup
git pull remote origin
git add notes/*.txt
git commit -m "Update notes"
git push origin master

