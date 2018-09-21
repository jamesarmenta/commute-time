import csv
from collections import defaultdict

averages = defaultdict(lambda: defaultdict(lambda: 0))

try:
    with open("./log.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            date, day, time, duration, route, text = line;
            time = int(round(float(int(time)*10) / float(100))*10) # Round time to closest whole
            # If it's 1760, it's actually 1800
            if (time + 40) % 100 == 0:
                time = time + 40
            # skip mornings for now
            if time < 1200:
                continue
            daytime = day + str(time);
            averages[daytime]['value'] = averages[daytime]['value'] + int(duration)
            averages[daytime]['count'] = averages[daytime]['count'] + 1
            averages[daytime]['route'+route] = averages[daytime]['route'+route] + 1
    f.close()

    final = []

    for daytime in averages:
        dt = averages[daytime]
        average = int(round(dt['value'] / dt['count']))
        routeCount = 0
        route = ''
        for key in dt:
            if 'route' in key:
                if dt[key] > routeCount:
                    routeCount = dt[key]
                    route = key
        final.append({
            'daytime': daytime,
            'route': route,
            'average': average
        })

    final = sorted(final, key=lambda k: k['daytime'])
    for i in final:
        print i['daytime'] + ',' + i['route'] + ',' + str(i['average'])

except Exception as e:
    print e
