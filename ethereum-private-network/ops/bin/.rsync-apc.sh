#!/bin/sh
echo "rsync to thangnguyen@172.16.126.135"
# rsync -arzP ../ myasoftpc:/home/thangnguyen/WORKING/eprivate.npt --exclude '' --delete
rsync -arzP ../ myasoftpc:/home/thangnguyen/WORKING/eprivate.npt --exclude '' --delete
