# Pysock 
## "Reverse Shell" in Python 3 (For Educational Purposes)
## Used modules:

* Socket
* Subprocess
* Requests
* OS
* Tkinter
* Pywin32

# Requirements

* Python 3

## Before attempting to compile with Pyinstaller, ensure all the used modules are installed

**

# PySocket Usage:

### NOTE: MAKE SURE TO CHANGE HOST & PORT VARIABLE IN CODE TO YOUR NEEDS

Compile the python file:

```
pyinstaller --clean -F <python-file-location>
```

1. Start a netcat listener on the desired port
```
nc -lvnp <port>
```

2. Run it on victim's machine, the promp will look like this:

![](/pics/vic.png)

3. The attacker's machine will get a connection & from here, there are 3 important features of this tool: **persistence**, **downloading files**, & **SQL file searching**

## Persistence feature

This feature will add a scheduled task onto the victim's machine that runs the executable every minute to ensure that even if you do lose your shell, you will get it back

NOTE: WINDOWS DEFAULTS THE SCHEDULED TASKS FEATURE TO ONLY EXECUTE TASKS IF THE COMPUTER IS CONNECTED TO POWER (CHARGING), SO THAT IS THE DEFAULT OF THIS. THIS CAN BE CHANGED VIA GUI, BUT AS FAR AS I KNOW IT CAN'T BE CHANGED VIA COMMAND LINE BESIDES USING AN XML FILE THAT HAS ALL THE DESIRED OPTIONS FOR THE SCHEDULED TASK, I PERSONALLY DIDN'T KNOW HOW TO IMPLEMENT THIS WITHOUT HAVING THE ATTACKER HAVE THE XML FILE ON THE VICTIM'S SYSTEM

The keyword to use for scheduling a task is *schedule* or *persist*, after entering either, you will be given a few questions to answer in order to schedule the task:

![](/pics/term.png)

![](/pics/term2.png)

The questions are:

1. The original file name of the exe. This is used to search for the file on the victim's system which is needed to schedule a task that will execute the file every minute.

2. The file path of the exe. This is given to you, you just need to enter it.

Once the task is scheduled, you can confirm it is ready to execute via *SCHTASKS* or *SCHTASKS /Query*

![](/pics/task.png)

The only reason ours says it couldn't start is because we already have our shell

## Downloading Feature

This feature will allow you to download files from the victim's system onto your own system.

The keywords to use are: *Download* or *download*

After entering Download, you're given a prompt:

![](/pics/term3.png)

Since you have to enter the file path of the file you wish to download, it's recommended that you enter ls and pwd & search for the file & verify the filepath beforehand

You're also asked to enter a port to listen on to receive the file, before entering the port make sure you've set up the listener & used this syntax:
```
nc -lvnp <port> > <desired-file-name>
```

![](/pics/term4.png)

After you enter the port you'll receive a connection & the file will be downloaded 
 
![](/pics/listen.png)

![](/pics/new.png)

## SQL & DB Search Feature

This feature is fairly self explanatory, it searches for any files with the *.sql* or *.db* extension & presents the path to you in case you wish to download them:

The keywords to use are: *sql* or *SQL*

![](/pics/smple.png) 

### NOTE: IF YOU ENTER A CMD INCORRECTLY OR A CMD THAT DOESN'T EXIST, THE ERROR WILL APPEAR IN THE VICTIM'S TERMINAL, EX:

We enter *clear* which isn't a cmd in Windows, our shell skips a line & returns nothing:

![](/pics/clr.png)

...but on the victim's machine:

![](/pics/vic2.png)

# Using the Dropper

Change out the *url, payloadName, and dropperName* values to whatever suits your purpose

* The *url* is where the payload (in this case, the Pysock reverse shell) should be located

* The *payloadName* is the name of the payload (in this case, the Pysock reverse shell)

* The *dropperName* is the name of the dropper, this variable is used to locate the dropper & display a popup to persuade the user to delete the dropper after executing it. This is implemented in the *popup* function & it exists because I couldn't figure out how to make the dropper delete itself.

Compile the dropper using Pyinstaller:

```
pyinstaller --clean -F <python-file-location>
```

I personally recommend using a site such as notabug.org if you can't use your own website to upload the reverse shell & host it:

* Create a repository on notabug.org

* Upload the reverse shell

* Click the reverse shell & right-click raw & click copy link

* Throw this link in the dropper.py file & compile it

# Execution of Dropper:

1. After executing the dropper, we get this popup:

![](/imgs2/img1.png)

2. We can go into the scheduled tasks to confirm our reverse shell is running...

![](/imgs2/schedule.png)

Boom! Our dropper grabs the new_winshell.exe file & schedules it to be executed!
