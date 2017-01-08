def convert(time):
    if len(str(time)) == 19:
        return str(time)[11:] + ",000"
    return str(time)[11:23].replace('.',',')
