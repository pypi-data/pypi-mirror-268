from datetime import datetime, timezone

class HuemulFunctions:
    def __init__(self):
        self.started = True
    
    #
    # getCurrentDateTime: returns current datetime
    # from version 1.1
    #
    def getCurrentDateTimeJava(self):
        return datetime.now(timezone.utc)

    # return datetime in log format
    # date: datetime.now(timezone.utc)
    # return string
    def getDateForLog(self, date):
        #dateTimeFormat: DateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss:SSS")
        dateString = date.isoformat(timespec='milliseconds')

        return dateString

    # return date in string format
    # date
    def getDateForApi(self):
        #dateTimeFormat: DateFormat = new SimpleDateFormat("yyyy-MM-ddTHH:mm:ss:SSSz")
        newDate = datetime.now(timezone.utc)
        dateString = newDate.isoformat(timespec='milliseconds')

        return dateString
    
    def getDifSeconds(self, dateFromIso, dateToIso):
        dateFrom = datetime.fromisoformat(dateFromIso)
        dateTo = datetime.fromisoformat(dateToIso)
        return (dateTo - dateFrom).total_seconds()
    
    def getDifMs(self, dateFromIso, dateToIso):
        dateFrom = datetime.fromisoformat(dateFromIso)
        dateTo = datetime.fromisoformat(dateToIso)
        return (dateTo - dateFrom).total_seconds() * 1000

    def deleteArgs(self, data):
        try:
            delattr(data, "args")
        except:
            a = None