import private_config
import googlemaps
import time
import sys

args = sys.argv;

# Reference
# https://developers.google.com/maps/documentation/directions/intro#DirectionsResponseElements

# MACROS
gmaps = googlemaps.Client(key=private_config.googleClientKey())
HOME = '3239 Zola St., San Diego CA 92106'
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
    duration_average = legs['duration']['text']
    duration_with_traffic = legs['duration_in_traffic']['text']

    return [str(summary), str(duration_average), str(duration_with_traffic)]

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
if "morning" in args:
    requested_commute = morning_commute

# Get the commute
try:
    commute_results = gmaps.directions(**requested_commute)
    # Print commute results
    printFormat(processResults(commute_results))
except Exception:
    # Error is in same index as duration_with_traffic
    # for visibility in Ubersicht 
    printFormat(['','','Error'])
