#!/bin/sh
DATE=`date '+%Y%m%d'`
COMMIT_MESSAGE="Logs for ${DATE}"

git add log.csv && git commit -m "${COMMIT_MESSAGE}" && git push
