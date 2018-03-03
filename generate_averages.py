try:
    f = open('~/Documents/commute-time/log.csv','r')

    averages = {
     'Mon':{},
     'Tue':{},
     'Wed':{},
     'Thu':{},
     'Fri':{},
     }

    for line in f:
        date,day,time,duration,route,text = line.splt(',');
        time = int(round(float(time*10) / float(100))*10) # Round time to closest whole
        print("time %s", time)
        averages[day][time][value] = (averages[day][time][value]*averages[day][time][count]) + duration
        averages[day][time][count]++;


    f.close()
except Exception as e:
    print e
