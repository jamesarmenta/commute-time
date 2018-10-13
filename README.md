# commute-time
A simple python script to monitor my commute time

```
*/10 7-9 * * 1-5 cd /home/pi/Documents/commute-time && python get_commute_time.py -morning -log
*/10 14-19 * * 1-5 cd /home/pi/Documents/commute-time && python get_commute_time.py -log
0 20 * * 1-5 cd /home/pi/Documents/commute-time && bash push_log_and_averages.sh
```
