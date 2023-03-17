# Welcome to Task Manager!

###### what is it about?

<!---inform the user what this project is about and what its capabilities are?--->
<sub>
Task Manager is a tool that allows you, <strong>The User</strong>, to keep track of any assignments due and promote
productivity towards your time managing skills. it allows you to plan out your tasks and let you know what needs to be worked on first as a priority rather than focus on assignments that can be done at the same day. 
</sub>

### How does it work?

<!---main is only importing taskgui lol-->

- `main.py`
  - <sub> starts up the task gui file [temporary program]</sub>
###### Gui Functionality

- `taskgui.py`
  - <sub>Runs the main window and every other function in the program. Basically the main function. </sub>
- `guifunctions.py`
  - <sub>Contains all GUI functions outside of the main window including popups and tabs.</sub>
- `taskcalendar.py`
  - <sub> Opens the calendar window from the main menu.</sub>

###### Attribute Functionality

- `task.py`
  - <sub>This has the class for an individual task, consisting of its name, date due, description. etc.</sub>

###### Import/Export Functionality

- `importToCSV.py`
  - <sub>Adds lines to the CSV file that's then read and used to display all tasks in the main menu.</sub>
- `exportCSV.py`
  <!----inform the user what the 'exporting as a csv file' is---->
  - <sub>This file is prompting the user that the csv file is in the path where the program is located.</sub>

###### Sorting Functionality

- `sortbyClass.py`
  <!----inform the user what the 'sorting by class' is---->
  - <sub> sorts the sample csv file,<strong>by class name</strong>, to a new file for the calendar list view</sub>
- `sortbyDueDate.py`
  <!----inform the user what the 'sorting by due dates' is---->
  - <sub> sorts the sample csv file,<strong>by date/time due</strong>, to a new file for the calendar list view</sub>
- `sortbyPriority.py`
  <!----inform the user what the 'sorting by priority' is---->
  - <sub> sorts the sample csv file,<strong>by priority</strong>, to a new file for the calendar list view</sub>

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
#Creates a blank csv to our temp "medium"
  pd.DataFrame({}).to_csv("medium.csv")
  taskCsv.to_csv('medium.csv',index=False)
  TC.cal_maker("medium.csv")

```

first, it is deleting the window calendar view list, if it is open, then it is going to read the task_list csv file so it can be sorted by pandas. it will then be appended to the new csv file called medium and calling the calendar view list function to create a new window with the sorted tasks based on a specific attribute (for instance, it is sorted by due date).


### Main Purpose of this Project?

<sub>This project gives users the ability to manage their tasks and assignments to better keep track of them and their time. It offers a variety of descriptors for tasks and allows users to set a date and time for which a task should be complete, which the user will be reminded of an hour or a few hours beforehand based on their preference.
</sub>


### How to start Program?

start the program via the main.py and taskgui.py should activate

<sub><strong>if the program is having issues with codespace, try running it via vscode and using 'pip install -r requirements.txt' in the shell command before running the program.</strong></sub>

### disclaimer:

for csv file, it must not be empty, please use the examples provided to prevent it from failing the porgram.

###### For test online:

https://replit.com/@CSCIPYTHON/Task-Manager?v=1

