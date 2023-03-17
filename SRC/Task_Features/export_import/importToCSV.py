import pandas as pd


def format_date(dict):
  yyyy= str(dict['year'] + 1900)
  mm = str(dict['month'] + 1)
  dd = str(dict['month_day'])
  
  # format so it's always mm/dd/yyyy
  if len(dd) == 1:
    dd = '0' + dd 
  if len(mm)  == 1:
    mm = '0'+ mm
  
  return f"{mm}/{dd}/{yyyy}" 

def format_time(dict):
    hour = str(dict['hour'])
    minute = str(dict['min'])
    sec = str(dict['sec'])

    if len(minute) == 1:
        minute = '0' + minute
    if len(hour) == 1:
        hour = '0' + hour
    if len(sec) == 1:
        sec = '0' + sec

    if int(hour) >= 12:
        if int(hour) > 12:
            hour = str(int(hour) - 12)
        timepart = "PM"
    else:
        if int(hour) == 0:
            hour = '12'
        timepart = "AM"

    return f"{hour}:{minute}:{sec}{timepart}"


def write_csv(task):
  name = getattr(task,'name')
  date = getattr(task,'date')
  time = getattr(task,'time')
  prior = getattr(task,'priority')
  type = getattr(task,'type')
  desc = getattr(task,'description')
  stat = getattr(task,'status')
  reminder_sent = False

  df = pd.DataFrame([(name, date, time, prior, desc, type, stat, reminder_sent)])
  df.to_csv('task_list.csv', mode='a', header=False, index=False)



