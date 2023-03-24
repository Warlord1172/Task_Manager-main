import sys
import datetime
import threading
import csv
from time import sleep
import time
from plyer import notification
import dearpygui.dearpygui as dpg
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import SRC.Task_Features.task as task
import SRC.Task_Features.export_import.importToCSV as iCSV

#imports year and month from datetime
current_month = int(datetime.datetime.now().month)
current_year = int(datetime.datetime.now().year)

#Set when to remind user about an assignment based on time from deadline
reminder_time = 1
tabCount = 0

#Prints each task as an individual tab
def printTabs(filename):
  file = pd.read_csv(filename)
  i = 0 
  global tabCount
  tabCount = 0
  with dpg.tab_bar(label='Tasks',tag='Task Bar', parent="Primary Window"):
    while (i < len(file)):
      with dpg.tab(label=file.iloc[i]['name']):
        dpg.add_text(f"Name: {file.iloc[tabCount]['name']}")
        dpg.add_text(f"Date Due: {file.iloc[tabCount]['date']}")
        dpg.add_text(f"Time Due: {file.iloc[tabCount]['time']}")
        dpg.add_text(f"Priority: {file.iloc[tabCount]['priority']}")
        dpg.add_text(f"Type: {file.iloc[tabCount]['type']}")
        dpg.add_text(f"Description: {file.iloc[tabCount]['description']}")
        dpg.add_text(f"Status: {file.iloc[tabCount]['status']}")
        dpg.add_text(f"Reminded?: {file.iloc[tabCount]['reminder_sent']}")
        #set buttons as "Mark as complete", "set to in-progress",and "Discard Task"
        with dpg.group(horizontal=True):
          dpg.add_button(label='Mark as complete',callback=set_to_complete,user_data=i)
          #set to in-progress button: should change the status on the specific tab item and update the main window
          dpg.add_button(label="set as In Progress",callback=set_to_progress,user_data=i)
          #discard task: erases the tab and will erase the tab item from the csv file.
          dpg.add_button(label="Discard Task",callback=discard_task,user_data=i)
      i+=1
      tabCount += 1


# Function to add new tabs as more tasks are added. 
def update_tabs(filename):
  file = pd.read_csv(filename)
  global tabCount
  if tabCount >= len(file):
    dpg.add_text("All the task are already displayed!")
    return
  with dpg.tab(label=file.iloc[tabCount]['name'],parent='Task Bar'):
    dpg.add_text(f"Name: {file.iloc[tabCount]['name']}")
    dpg.add_text(f"Date Due: {file.iloc[tabCount]['date']}")
    dpg.add_text(f"Time Due: {file.iloc[tabCount]['time']}")
    dpg.add_text(f"Priority: {file.iloc[tabCount]['priority']}")
    dpg.add_text(f"Type: {file.iloc[tabCount]['type']}")
    dpg.add_text(f"Description: {file.iloc[tabCount]['description']}")
    dpg.add_text(f"Status: {file.iloc[tabCount]['status']}")
    dpg.add_text(f"Reminded?: {file.iloc[tabCount]['reminder_sent']}")
    with dpg.group(horizontal=True):
      dpg.add_button(label='Mark as complete', callback=set_to_complete, user_data=tabCount)
      dpg.add_button(label="set as In Progress", callback=set_to_progress, user_data=tabCount)
      dpg.add_button(label="Discard Task", callback=discard_task, user_data=tabCount)
    tabCount += 1
  
  
#identify tab name, use "Mark as complete","Set to In Progress", and "Discard Task" buttons to change attributes to the assignment attributess
''' this means adding a tag to every item iterated from print tabs function, then performing these tasks to that tag'''


def set_to_complete(sender, data, user_data):
    lines = list()
    with open('task_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
    lines[user_data+1][6] = "Done"
    with open('task_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    dpg.delete_item("Task Bar")
    printTabs("task_list.csv")

def set_to_progress(sender, data, user_data):
    lines = list()
    with open('task_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
    lines[user_data+1][6] = "In Progress"
    with open('task_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    dpg.delete_item("Task Bar")
    printTabs("task_list.csv")

def discard_task(sender, data, user_data):
    global tabCount
    tabCount -= 1
    lines = list()
    with open('task_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
    del lines[user_data+1]
    with open('task_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    dpg.delete_item("Task Bar")
    printTabs("task_list.csv")



def create_new_PW():
  #made to copy popup window (import assignments window)
  with dpg.window(label="Import Assignments",
                  tag="Popup Window",
                  on_close=destroy_import_module):
    dpg.add_text("Class attributes")
    with dpg.group(horizontal=True):
      dpg.add_date_picker(label="date due",
                          tag='Date',
                          default_value={'year': current_year - 1900})
      dpg.add_time_picker(label="Time due",
                          tag='Time',
                          default_value={
                            'hour': 00,
                            "min": 00
                          })
    dpg.add_input_text(label='Name', tag='Name')
    dpg.add_input_text(label='Assignment Description', tag='Description')
    dpg.add_input_text(label='Type(for what class?)', tag='Type')
    dpg.add_radio_button(label='Status',
                         tag='Status',
                         items=["Not Done", "In Progress", "Done"],
                         horizontal=True,
                         default_value="Not Done")
    dpg.add_radio_button(
      label="Priority",
      tag='Priority',
      items=["Non-important", "Semi-important", "Priority-important"],
      horizontal=True,
      default_value="Non-important")
    with dpg.group(horizontal=True):
      dpg.add_button(label='Save and Exit', callback=save_ex)
      dpg.add_button(label='Save and Add more', callback=save_addpass)
      dpg.add_button(label='Exit Without Saving',
                     callback=destroy_import_module)



#tester to see if button works(placeholder)
def print_me(sender, app_data):
  print(f"Menu Item: {sender},{app_data}")
###########################################

  
def destroy_popup():
  dpg.delete_item("Reminder")


def destroy_import_module():
  dpg.delete_item("Popup Window")


def destroy_main():
  #dpg.delete_item("Primary Window")
  dpg.stop_dearpygui()
  dpg.set_main_thread_should_stop()
  sys.exit()
  

def destroy_error():
  dpg.delete_item("error")

def delete_disclaimer():
  dpg.delete_item("Disclaimer")

def grab_attributes(sender, app_data):
  t_name = dpg.get_value("Name")
  t_desc = dpg.get_value("Description")
  t_prior = dpg.get_value("Priority")
  t_stat = dpg.get_value("Status")
  t_dueD = dpg.get_value("Date")
  t_dueT = dpg.get_value("Time")
  t_type = dpg.get_value("Type")

  ## Format date and time properly
  t_dueD = iCSV.format_date(t_dueD)
  t_dueT = iCSV.format_time(t_dueT)
  #print(f"{t_dueD}\n\n{t_dueT}")
  #format : name,date,time,priority,type,description,status
  tempTask = task.Task(t_name, t_dueD, t_dueT, t_prior, t_type, t_desc, t_stat, False)  # Add False for reminder sent
  #Task class attributes:
  #name, date, time, priority, class type, description,status
  iCSV.write_csv(tempTask)


def save_ex(sender, app_data):
  if dpg.get_value("Name"):
    grab_attributes(sender, app_data)
    destroy_import_module()
    dpg.delete_item("Task Bar")
    printTabs("task_list.csv")
  else:
    with dpg.window(label="Error", tag="error"):
      dpg.add_text("Can't add assignment without a name!")
      dpg.add_button(label="Ok", callback=destroy_error)


def save_addpass(sender, app_data):
  if dpg.get_value("Name"):
    grab_attributes(sender, app_data)
    recycle_window()
    dpg.delete_item("Task Bar")
    printTabs("task_list.csv")
  else:
    with dpg.window(label="Error", tag="error"):
      dpg.add_text("Can't add assignment without a name!")
      dpg.add_button(label="Ok", callback=destroy_error)


def recycle_window():
  dpg.delete_item("Popup Window")
  create_new_PW()


def launcher():
  d = threading.Thread(target=background_check_reminders)
  d.start()


def background():
  while True:
    "refreshing..."
    sleep(10.0)


#this window should determine how much time when the date is due as well as functionality of what specified time would the user like to be reminded (may need a local attribute for that to be functional)
#################################reminder window###################################################

def reminder_win(rem_num):
    # Load the tasks from the CSV file
    file = pd.read_csv("task_list.csv")

    # Get the current date and time
    now = datetime.datetime.now()

    # Iterate through the tasks
    for index, row in file.iterrows():
        task_due_date_str = row["date"]
        task_due_time_str = row["time"]
        task_name = row["name"]

        # Convert the task due date and time to a datetime object
        task_due_datetime = datetime.datetime.strptime(task_due_date_str + " " + task_due_time_str, "%m/%d/%Y %H:%M:%S%p")

        # Calculate the time difference between the current time and the task due time
        time_difference = task_due_datetime - now

        # Check if the time difference is less than or equal to the reminder time
        if time_difference.total_seconds() <= rem_num * 3600:  # Convert hours to seconds
            hours_left = int(time_difference.total_seconds() // 3600)
            minutes_left = int((time_difference.total_seconds() % 3600) // 60)

            # Show a reminder popup window
            with dpg.window(label="Notification Window", tag="Reminder"):
                dpg.add_text(f"This is a notification that {task_name} is due in {hours_left} hours and {minutes_left} minutes!")
                dpg.add_button(label="Ok", callback=destroy_popup)
            return True

    return False

###################################################################################################
#make disclaimer if tabs does not load in properly
def disclaimer():
  with dpg.window(label="Disclaimer", tag="Disclaimer"):
    dpg.add_text("If the tabs are incorrect or did not work properly\n after importing a class, please restart the program to see the effects...")
    dpg.add_button(label="Ok",callback=delete_disclaimer)
    
    

def background_check_reminders():
    while True:
        time.sleep(60)
        task_list = pd.read_csv("task_list.csv")

        for index, row in task_list.iterrows():
            task_due_date_str = row[1]
            task_due_time_str = row[2]
            reminder_sent = row["reminder_sent"]

            task_due_datetime = datetime.datetime.strptime(task_due_date_str + " " + task_due_time_str, "%m/%d/%Y %I:%M:%S%p")
            current_datetime = datetime.datetime.now()
            reminder_sent = row[7]

            if current_datetime >= task_due_datetime - datetime.timedelta(minutes=30) and not reminder_sent:
              task_name = row[0]
              time_difference = task_due_datetime - current_datetime
              hours_left = int(time_difference.total_seconds() // 3600)
              minutes_left = int((time_difference.total_seconds() % 3600) // 60)
              show_tkinter_message_box('Assignment Reminder', f"{task_name} is due in {hours_left} hours and {minutes_left} minutes!")  # Show a tkinter message box with remaining time
              task_list.at[index, "reminder_sent"] = True
              task_list.to_csv('task_list.csv', index=False)

def show_tkinter_message_box(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo(title, message)
    root.destroy()  # Close the main window when the message box is closed
