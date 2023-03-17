import pandas as pd
import SRC.Calendar_Features.Taskcalendar as TC
import dearpygui.dearpygui as dpg

def sortDueDate(filen):
    dpg.delete_item("Cal Window")
    taskCsv = pd.read_csv(filen)
    taskCsv.sort_values(["date"],
                        inplace=True)
    pd.DataFrame({}).to_csv("medium.csv")
    taskCsv.to_csv('medium.csv', index=False)
    return "medium.csv"


def sortPriority(filen):
    dpg.delete_item("Cal Window")
    taskCsv = pd.read_csv(filen)
    taskCsv.sort_values(["priority"],
                        inplace=True)
    pd.DataFrame({}).to_csv("medium.csv")
    taskCsv.to_csv('medium.csv', index=False)
    return "medium.csv"


def sortStatus(filen):
    dpg.delete_item("Cal Window")
    taskCsv = pd.read_csv(filen)
    taskCsv.sort_values(["status"],
                        inplace=True)
    pd.DataFrame({}).to_csv("medium.csv")
    taskCsv.to_csv('medium.csv', index=False)
    return "medium.csv"


