def write_to_log(dataToPrint):
    try:
        # Open log file
        f = open("./log.csv", "a+");

        # Print each param, comma separated
        for item in dataToPrint[:-1]:
            f.write("%s," % item)

        # Except for the last one - no trailing comma
        f.write("%s" % dataToPrint[-1])

        # New line for the next guy
        f.write("\n")

        f.close();
    except Exception as e:
        print e
