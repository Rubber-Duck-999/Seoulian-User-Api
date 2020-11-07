import datetime

def getTime():
    date = datetime.datetime.now()
    newDate = date.strftime('%Y-%m-%d %H:%M:%S')
    return newDate