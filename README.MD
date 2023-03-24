# Welcome to Task Manager!

Make sure to allow the exe file to device (From Windows Defender) to use this program. it is not a virus, i promise!

###### what is it about?

<!---inform the user what this project is about and what its capabilities are?--->
<sub>
Task Manager is a tool that helps you, <strong>The User</strong>, to keep track of your assignments and improve your time management skills. It allows you to plan out your tasks and prioritize them based on their due dates. By focusing on tasks that are due soon, you can effectively manage your time and avoid last-minute rushes.
</sub>

### How does it work?

<!---main is only importing taskgui lol-->

- `main.py`
  - <sub>Starts up the task GUI file (temporary program)</sub>
###### Gui Functionality

- `taskgui.py`
  - <sub>Runs the main window and manages all other functions in the program.</sub>
- `guifunctions.py`
  - <sub>Contains all GUI functions outside of the main window, including pop-ups and tabs.</sub>
- `taskcalendar.py`
  - <sub> Opens the calendar window from the main menu.</sub>

###### Attribute Functionality

- `task.py`
  - <sub>Contains the class for an individual task, consisting of its name, due date, description, etc.</sub>

###### Import/Export Functionality

- `importToCSV.py`
  - <sub>Adds lines to the CSV file, which is then read and used to display all tasks in the main menu.</sub>
- `exportCSV.py`
  <!----inform the user what the 'exporting as a csv file' is---->
  - <sub>Informs the user that the CSV file is located in the path where the program is running.</sub>

###### Sorting Functionality

- `sortbyClass.py`
  <!----inform the user what the 'sorting by class' is---->
  - <sub> Sorts the sample CSV file<strong>by class name </strong>for the calendar list view.</sub>
- `sortbyDueDate.py`
  <!----inform the user what the 'sorting by due dates' is---->
  - <sub>Sorts the sample CSV file <strong>by due date</strong> and time for the calendar list view.</sub>
- `sortbyPriority.py`
  <!----inform the user what the 'sorting by priority' is---->
  - <sub> Sorts the sample CSV file <strong>by priority</strong> for the calendar list view.</sub>

### Examples?

<sub> For examples, we will be showing you what type of sorting this program will do when showing a specific format on what tasks are due before others, or seeing how the tabs are being printed onto the main menu. </sub>
<!----inform the user what sorting algorithms are implemented (preferably sort by due date, or the print tabs function)-->

```
import pandas as pd
import SRC.Calendar_Features.Taskcalendar as TC
import dearpygui.dearpygui as dpg

def sortDueDate():
  dpg.delete_item("Cal Window")
  taskCsv = pd.read_csv("task_list.csv")
  taskCsv.sort_values(["date"],inplace = True)
  # Creates a blank CSV to store the sorted data temporarily
  pd.DataFrame({}).to_csv("medium.csv")
  taskCsv.to_csv('medium.csv',index=False)
  TC.cal_maker("medium.csv")

```

The function first deletes the calendar window view list, if open. It then reads the 'task_list.csv' file and sorts it using pandas. The sorted data is then appended to a new CSV file called 'medium.csv', and the calendar view list function is called to create a new window with the sorted tasks based on their due dates.


### Main Purpose of this Project?

<sub>This project aims to help users manage their tasks and assignments more effectively by providing an organized and intuitive interface. Users can set due dates and times for tasks and receive reminders ahead of time, based on their preferences. This ensures that users stay on top of their tasks and manage their time efficiently.
</sub>


### How to start Program?

Start the program by running 'main.py', which will activate 'taskgui.py'

<sub><strong>If the program encounters issues with codespace, try running it via VSCode and use the command pip install -r requirements.txt in the terminal before running the program.</strong></sub>

### disclaimer:

You must have a python environment and download the libraries to use this program

###### For test online:

You can test the Task Manager online here: https://replit.com/@CSCIPYTHON/Task-Manager?v=1