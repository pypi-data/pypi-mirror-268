
import requests,re,datetime
from .schedule import schedule
from .scheduleitem import scheduleitem

class zermelo:
    def __init__(self, school, username,password=None, version=3,debug=False,teacher=False):
        self.school = school
        self.username = username
        self.password = password
        self.version = version
        self.debug = debug
        self.teacher = teacher
        self.base_url = f"https://{self.school}.zportal.nl/api/v{self.version}/"
        self.session = requests.Session()
        self.login()
    def get_date(self):
        now = datetime.datetime.now()
        return (now.year,now.isocalendar()[1],int((datetime.datetime.fromtimestamp(now.timestamp()) - datetime.datetime.utcfromtimestamp(now.timestamp())).total_seconds() / 3600))
    

    def login(self):
        token = re.search("code=[0-z]*",self.session.post(f"{self.base_url}oauth?tenant={self.school}&client_id=OAuthPage&redirect_uri=/main/&scope=&state=4E252A&response_type=code&username={self.username}&password={self.password}",allow_redirects=False).headers["location"]).group()[5::]
        self.access_token = self.session.post(f"{self.base_url}oauth/token?code={token}&client_id=ZermeloPortal&client_secret=42&grant_type=authorization_code&rememberMe=False").json()["access_token"]
        self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})
    def get_raw_scedule(self,year=0,week=0,datemode="absolute"):
        tyear, tweek,_ = self.get_date()
        if datemode == "absolute":
            if year == 0:
                year = tyear
            if week == 0:
                week = tweek
        elif datemode == "relative":
            year += tyear
            week += tweek
            if week > 52:
                year += week % 52
                week = 52
            if week < 1:
                year -= week % 52
                week = 1
            
        return self.session.get(f"{self.base_url}liveschedule?{'teacher' if (self.teacher) else 'student'}={self.username}&week={year}{week:0>2}").json()
    def get_schedule(self,week=0,year=0,datemode="absolute") -> schedule:
        return schedule(self.get_raw_scedule(week=week,year=year,datemode=datemode),self)
    def enroll(self,id = None,action = None):
        if action is not None:
            return action.enroll()
        elif id is not None:
            return self.session.post(f"{self.base_url}liveschedule/enrollment?enroll={id}&unenroll=").json()
    def unenroll(self,id = None,action = None):
        if action is not None:
            return action.unenroll()
        elif id is not None:
            return self.session.post(f"{self.base_url}liveschedule/enrollment?unenroll=&enroll={id}").json()
    def __repr__(self) -> str:
        return self.get_schedule().__repr__()