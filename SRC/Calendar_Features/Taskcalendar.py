import dearpygui.dearpygui as dpg
import SRC.Task_Features.Sorting_Features.sortingmethods as sm
import pandas as pd

def cal_maker(filen):
    file = pd.read_csv(filen)
    with dpg.window(tag="Cal Window", label="Calendar", no_close=True):
        with dpg.table(header_row=True, resizable=True, borders_innerV=True, borders_outerV=True):
            dpg.add_table_column(label="Name")
            dpg.add_table_column(label="Date Due")
            dpg.add_table_column(label="Time Due")
            dpg.add_table_column(label="Priority")
            dpg.add_table_column(label="Status")

            for index, row in file.iterrows():
                with dpg.table_row():
                    dpg.add_text(row['name'])
                    dpg.add_text(row['date'])
                    dpg.add_text(row['time'])
                    dpg.add_text(row['priority'])
                    dpg.add_text(row['status'])

        with dpg.group(horizontal=True):
            dpg.add_button(label="Sort by Due Date", callback=lambda sender, data: cal_maker(sm.sortDueDate(filen)))
            dpg.add_button(label="Sort by Status", callback=lambda sender, data: cal_maker(sm.sortPriority(filen)))
            dpg.add_button(label="Sort by Priority", callback=lambda sender, data: cal_maker(sm.sortStatus(filen)))
            dpg.add_button(label="Exit", callback=delete_cal)

def delete_cal():
    dpg.delete_item("Cal Window")

def cal_safe():
    cal_maker("task_list.csv")
