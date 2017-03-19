import bluetooth
import random
import socket
import subprocess
#import RPi.GPIO as gpio 
#
#gpio.setmode(gpio.BCM)
#gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_DOWN)
#gpio.setup(24, gpio.IN, pull_up_down=gpio.PUD_UP)


MacBank = open("caught.txt", "w+")


storedMonsters = MacBank.readlines()

#Get all devices in the area
deviceList = bluetooth.discover_devices()

while (len(storedMonsters) < 3):


    #Display all the addresses


    subprocess.call(['sudo','python2','write_minishift.py',"You've found "+str(len(deviceList))+" MAC address"])

    if (len(deviceList) <=0):
        print("Not enough devices!")
        break


    #Randomly pick one from the list
    rand = random.randint(0, len(deviceList)-1)

    
    print(rand)
    pickedDevice = deviceList[rand]
    

    #Show it to the user
    print(": ")
    print(pickedDevice)

    subprocess.call(['sudo','python2','write_minishift.py',str(pickedDevice)+" is close enough to catch!    Catch it?"])
    print("Pick?")


    #Pick or decline

    picked = None

    i = input()
    if (i == "y"):
        picked = True
    elif (i == "n"):
        picked = False

#    while(gpio.input(23) == 0 and gpio.input(24) == 1):
#
#        if gpio.input(23) == 1:
#            picked = True
#        elif gpio.input(24) == 0:
#            picked = False

    if picked == True:
        print ("You picked: "+str(pickedDevice))
        subprocess.call(['sudo','python2','write_minishift.py',"You picked "+str(pickedDevice)+"!"])


    #checkForButtonYes()

    #Remove from deviceList

    deviceList.remove(pickedDevice)

    #add to pocket
    if picked == True:
        storedMonsters.append(pickedDevice)
        MacBank.write(str(pickedDevice)+"\n")



print ("You've got "+str(storedMonsters))
print ("Pick a MACMonster to send to FIGHT")

pickedDevice = None
for device in storedMonsters:

    print(device)

    i = input()
    if (i == "y"):
        pickedDevice = device
    elif (i == "n"):
        pickedDevice = device

print (pickedDevice)

#Connect to server
sock = socket.socket()
host = "localhost"
port = 1337

sock.connect((host,port))


sock.send(str(pickedDevice).encode())

#Check if other people connected
#Send MAC address
#Wait until we're told we've won


