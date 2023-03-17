import tkinter as tk,os,shutil
from tkinter import filedialog,messagebox as mb
def saved_csv():
    root = tk.Tk()
    root.withdraw()
    template_csv = os.path.join(os.getcwd(), 'task_list.csv')
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[("CSV Files", "*.csv")],initialdir=os.getcwd(),initialfile=template_csv)
    if file_path:
        # code to create and save the CSV file at the selected location
        shutil.copy(template_csv, file_path)
    else:
        mb.showinfo('info',"Save CSV file has been cancelled")
  #with dpg.window(label="Export CSV Notice", tag="excsv"):
  #  dpg.add_text("the file is saved in this program's path location.\nTo send in a new csv file, please use the same filename as the file you have extracted\n then insert it back to the program's path location.")
  #  dpg.add_button(label="Ok",callback=destroy_excsv)
import dearpygui as dpg
def destroy_excsv():
  dpg.delete_item("excsv")