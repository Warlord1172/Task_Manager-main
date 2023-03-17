import datetime

class Task:
  def __init__(self, name, date=(datetime.date.today()).strftime("%m/%d/%Y"), time="23:59:59", priority="low", type="math", description="", status="incomplete", reminder_sent=False):
        self.name = name
        self.date = date
        self.time = time
        self.priority = priority
        self.type = type
        self.description = description
        self.status = status
        self.reminder_sent = reminder_sent

  def set_status(self, stat):
    self.status = stat

  def change_name(self, str):
    self.name = str

  def change_date(self, dat):
    self.date = dat

  def change_time(self, time):
    self.time = time
    
  def change_priority(self, prior):
    self.priority = prior

  def change_Ctype(self, typ):
    self.type = type
    
  # Add a new method to set reminder_sent
  def set_reminder_sent(self, sent):
    self.reminder_sent = sent

def create_task():
  pass