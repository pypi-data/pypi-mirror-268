
import datetime
import pytz

from .scheduleaction import scheduleaction


class scheduleitem:
    def __init__(self,json,main) -> None:
        self.session = main
        self.json = json
        if len(self.json["status"]) > 0:
            self.statuscode = self.json["status"][0]["code"]
            self.statustext = self.json["status"][0]["en"]
        else:
            self.statuscode = None
            self.statustext = None
        self.actions = [scheduleaction(action,self.session) for action in self.json["actions"]]
        self.start = datetime.datetime.fromtimestamp(self.json["start"],pytz.timezone("UTC")).astimezone(pytz.timezone("europe/amsterdam"))
        self.end = datetime.datetime.fromtimestamp(self.json["end"],pytz.timezone("UTC")).astimezone(pytz.timezone("europe/amsterdam"))
        self.cancelled = self.json["cancelled"]
        self.appointmenttype = self.json["appointmentType"]
        self.online = self.json["online"]
        self.optional = self.json["optional"]
        self.appointmentinstance = self.json["appointmentInstance"]
        self.starttimeslotname = self.json["startTimeSlotName"]
        self.endtimeslotname = self.json["endTimeSlotName"]
        self.subjects = self.json["subjects"]
        self.groups = self.json["groups"]
        self.locations = self.json["locations"]
        self.teachers = self.json["teachers"]
        self.onlineteachers = self.json["onlineTeachers"]
        self.onlinelocationurl = self.json["onlineLocationUrl"]
        self.capacity = self.json["capacity"]
        self.expectedstudentcount = self.json["expectedStudentCount"]
        self.expectedstudentcountonline = self.json["expectedStudentCountOnline"]
        self.changedescription = self.json["changeDescription"]
        self.schedulerremark = self.json["schedulerRemark"]
        self.content = self.json["content"]
        self.creator = self.json["creator"]
        self.id = self.json["id"]
        self.status = self.statuscode, self.statustext
    def __repr__(self) -> str:
        return f"{','.join(self.subjects): <4} {','.join(self.teachers): <4} {self.start.strftime('%T')}-{self.end.strftime('%T')} {self.id}\n"
