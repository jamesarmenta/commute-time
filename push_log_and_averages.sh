#!/usr/bin/env bash
DATE=`date '+%Y%m%d'`
git add log_evening.csv
git add log_morning.csv
git commit -m "Commute data for ${DATE}"
git push
