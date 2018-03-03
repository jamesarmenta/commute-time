#!/usr/bin/env bash
DATE=`date '+%Y%m%d'`
git add log.csv
git commit -m "Commute data for ${DATE}"
git push
