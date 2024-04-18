import datetime

import pytz


class scheduleaction:
    def __init__(self,json,main) -> None:
        self.main = main
        self.json = json
        if len(self.json["status"]) > 0:
            self.statuscode = self.json["status"][0]["code"]
            self.statustext = self.json["status"][0]["en"]
        else:
            self.statuscode = None
            self.statustext = None
        if self.json["appointment"] != None:
            # timezone = pytz.timezone(datetime.datetime.now().astimezone().tzname())
            self.start = datetime.datetime.fromtimestamp(self.json["appointment"]["start"],pytz.timezone("UTC")).astimezone(pytz.timezone("europe/amsterdam"))
            self.end = datetime.datetime.fromtimestamp(self.json["appointment"]["end"],pytz.timezone("UTC")).astimezone(pytz.timezone("europe/amsterdam"))
            self.cancelled = self.json["appointment"]["cancelled"]
            self.plannedattendance = self.json["appointment"]["plannedAttendance"]
            self.studentenrolled = self.json["appointment"]["studentEnrolled"]
            self.allowedactions = self.json["appointment"]["allowedActions"]
            self.optional = self.json["appointment"]["optional"]
            self.attendanceoverruled = self.json["appointment"]["attendanceOverruled"]
            self.appointmenttype = self.json["appointment"]["appointmentType"]
            self.online = self.json["appointment"]["online"]
            self.onlinelocationurl = self.json["appointment"]["onlineLocationUrl"]
            self.appointmentinstance = self.json["appointment"]["appointmentInstance"]
            self.starttimeslotname = self.json["appointment"]["startTimeSlotName"]
            self.endtimeslotname = self.json["appointment"]["endTimeSlotName"]
            self.subjects = self.json["appointment"]["subjects"]
            self.groups = self.json["appointment"]["groups"]
            self.locations = self.json["appointment"]["locations"]
            self.teachers = self.json["appointment"]["teachers"]
            self.onlineteachers = self.json["appointment"]["onlineTeachers"]
            self.capacity = self.json["appointment"]["capacity"]
            self.expectedstudentcount = self.json["appointment"]["expectedStudentCount"]
            self.expectedstudentcountonline = self.json["appointment"]["expectedStudentCountOnline"]
            self.changedescription = self.json["appointment"]["changeDescription"]
            self.schedulerremark = self.json["appointment"]["schedulerRemark"]
            self.content = self.json["appointment"]["content"]
            self.creator = self.json["appointment"]["creator"]
            self.availablespace = self.json["appointment"]["availableSpace"]
            self.id = self.json["appointment"]["id"]
        else:
            self.start = None
            self.end = None
            self.cancelled = None
            self.plannedattendance = None
            self.studentenrolled = None
            self.allowedactions = None
            self.optional = None
            self.attendanceoverruled = None
            self.appointmenttype = None
            self.online = None
            self.onlinelocationurl = None
            self.appointmentinstance = None
            self.starttimeslotname = None
            self.endtimeslotname = None
            self.subjects = None
            self.groups = None
            self.locations = None
            self.teachers = None
            self.onlineteachers = None
            self.capacity = None
            self.expectedstudentcount = None
            self.expectedstudentcountonline = None
            self.changedescription = None
            self.schedulerremark = None
            self.content = None
            self.creator = None
            self.availablespace = None
            self.id = None
            
        self.allowed = self.json["allowed"]
        self.post = self.json["post"]
    def enroll(self):
        return self.main.session.post(f"{self.main.base_url}liveschedule/enrollment?enroll={self.id}&unenroll=").json()
    def unenroll(self):
        return self.main.session.post(f"{self.main.base_url}liveschedule/enrollment?unenroll=&enroll={self.id}").json()
    def toggle_enroll(self):
        return self.main.session.post(f"{self.main.base_url}{self.post[8::]}").json()
    def __repr__(self) -> str:
        return f"subjects={self.subjects},teachers={self.teachers},start={self.start},end={self.end},cancelled={self.cancelled},allowed={self.allowed},id={self.id}"
        
        