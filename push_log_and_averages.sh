#!/usr/bin/env bash
DATE=`date '+%Y%m%d'`
python generate_averages.py
git add averages_evening.txt
git add averages_morning.txt
git add log_evening.csv
git add log_morning.csv
git commit -m "Commute data and updated averages for ${DATE}"
git push
