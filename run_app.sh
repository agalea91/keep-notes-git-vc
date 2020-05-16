#!/bin/bash

echo "Updating local filestore"
docker-compose up --build

echo "Updated remote filestore"
cd ~/Keep\ Notes\ Backup \
   && git add notes/*.txt \
   && git commit -m "Update notes" \
   && git push origin master

