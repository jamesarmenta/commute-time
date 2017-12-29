import private_config
import googlemaps
import time

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
commute_morning, commute_evening = commute_common.copy(), commute_common.copy()

# commute_morning.update({'origin': HOME, 'destination': WORK})
commute_evening.update({'origin': WORK, 'destination': HOME})
# morning_results = gmaps.directions(**commute_morning)
try:
    evening_results = gmaps.directions(**commute_evening)
    printFormat(processResults(evening_results))
except Exception:
    # Error is in same index as duration_with_traffic
    # for visibility in Ubersicht 
    printFormat(['','','Error'])
