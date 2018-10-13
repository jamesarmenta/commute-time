import private_config
from write_to_log import write_to_log
import googlemaps
import time
import datetime
import sys

args = sys.argv;

# Reference
# https://developers.google.com/maps/documentation/directions/intro#DirectionsResponseElements

# MACROS
gmaps = googlemaps.Client(key=private_config.googleClientKey())
HOME = '1303 W Lewis Street, San Diego, CA 92103'
WORK = '7535 Torrey Santa Fe Rd, San Diego, CA 92129'

def printFormat(arr):
    for i in arr:
        print i

def createDict(*args):
     return dict(((k, eval(k)) for k in args))

def processResults(results):
    # Summary for route like I-5 S or I-163
    summary = results[0]['summary']

    legs = results[0]['legs'][0]
    duration_in_seconds = legs['duration_in_traffic']['value']
    duration_with_traffic = legs['duration_in_traffic']['text']

    now = datetime.datetime.now()
    result_date = now.strftime('%Y%m%d')
    result_day = now.strftime('%a')
    result_time = now.strftime('%H%M')

    return [str(result_date), str(result_day), str(result_time), str(duration_in_seconds), str(summary), str(duration_with_traffic)]

# PARAMS ------------------
now = lambda: int(time.time())
departure_time = str(now())
mode = 'driving'
traffic_model = 'best_guess'

# COMMUTES ------------------
commute_common = createDict('departure_time', 'mode', 'traffic_model');
morning_commute, evening_commute = commute_common.copy(), commute_common.copy()

morning_commute.update({'origin': HOME, 'destination': WORK})
evening_commute.update({'origin': WORK, 'destination': HOME})

# Assume evening commute
requested_commute = evening_commute
# Unless morning was passed in as an arg
if '-morning' in args:
    requested_commute = morning_commute

# Get the commute
try:
    commute_results = gmaps.directions(**requested_commute)
    # Print commute results
    results = processResults(commute_results)
    printFormat(results)
    # Save to log if told to do so
    if '-log' in args:
        if '-morning' in args:
            # a+ to append
            write_to_log(results, './log_morning.csv')
        else:
            write_to_log(results, './log_evening.csv')
except Exception as e:
    print("Error")
    # print(e)
