import datetime

def getTime():
    date = datetime.datetime.now()
    newDate = date.strftime("%x")
    print(date)
    return newDate