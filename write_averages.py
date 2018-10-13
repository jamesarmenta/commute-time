def write_averages(dataToPrint, filename):
    try:
        # Open log file
        f = open(filename, 'w');

        # Print each param, comma separated
        for item in dataToPrint:
            f.write("%s\n" % item)

        f.close();
    except Exception as e:
        print e
