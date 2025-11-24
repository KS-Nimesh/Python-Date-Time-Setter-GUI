import subprocess
from datetime import datetime
from tkinter import *
from tkinter import messagebox

def main_func():
    time=inputfield_time.get()
    date=inputfield_date.get()

    new_dt=f"{date} {time}"

    sys_date=datetime.now().strftime("%Y-%m-%d")
    sys_time=datetime.now().strftime("%H:%M:%S")
    
    if(sys_date==date and sys_time==time):
        messagebox.showinfo("System date and time match with you enterd ")
    else:
        messagebox.showwarning("WARNING","system time or date is incorrect  !!!!!\n Starting change time and Date ....")
        try:
            subprocess.run(["sudo", "date", "-s", new_dt],check=True)
            messagebox.showinfo("Sucuessfuly", "set time and date")
        except Exception as error:
            messagebox.showerror("ERROR","List of errors",error)
            
def ctd():
 sys_date=datetime.now().strftime("%Y-%m-%d")
 sys_time=datetime.now().strftime("%H:%M:%S")
 sys_dt=f"{sys_date} {sys_time}"
 messagebox.showinfo("System Date & Time",sys_dt)
 

#gui
root =Tk()
root.title("Time & Date checker/Setter")
root.geometry("400x200")

Label(root,text="Enter time (yyyy-mm-dd)").pack(pady=5)
inputfield_time=Entry(root)
inputfield_time.pack(pady=5)

Label(root,text="Enter date (HH:MM:SS)").pack(pady=5)
inputfield_date=Entry(root)
inputfield_date.pack(pady=5)

button_frame=Frame(root)
button_frame.pack(pady=10)

Button(button_frame,text="Set T & D",command=main_func).pack(side=LEFT,pady=2)
Button(button_frame,text="Current T/D",command=ctd).pack(side=LEFT,pady=2)
Button(button_frame,text="Exit",command=root.quit).pack(side=LEFT,pady=6)

root.mainloop()

