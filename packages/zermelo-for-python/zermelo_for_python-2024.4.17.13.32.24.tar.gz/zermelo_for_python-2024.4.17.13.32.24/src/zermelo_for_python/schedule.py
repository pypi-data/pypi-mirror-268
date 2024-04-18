from .scheduleitem import scheduleitem
class schedule:
    def __init__(self,json,main) -> None:
        self.session = main
        self.json = json["response"]
        self.status = self.json["status"]
        self.message = self.json["message"]
        self.details = self.json["details"]
        self.eventId = self.json["eventId"]
        self.startRow = self.json["startRow"]
        self.endRow = self.json["endRow"]
        self.totalRows = self.json["totalRows"]
        self.week = self.json["data"][0]["week"]
        self.user = self.json["data"][0]["user"]
        self.appointments = [scheduleitem(appointment,self.session) for appointment in self.json["data"][0]["appointments"]]
    def __repr__(self) -> str:
        result = ""
        pstart = ""
        for i in self.appointments:
            if i.start.strftime("%D") != pstart:
                pstart = i.start.strftime("%D")
                result += f"\n\n{pstart}\n"
            if (not i.cancelled) and i.id != None:
                result += i.__repr__()
        return result
    