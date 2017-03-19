import bluetooth
import random
import socket
import subprocess
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(24, gpio.IN, pull_up_down=gpio.PUD_UP)


MacBank = open("caught.txt", "w+")


storedMonsters = MacBank.readlines()

#Get all devices in the area
deviceList = bluetooth.discover_devices()

while (len(storedMonsters) < 3):


    #Display all the addresses
    print("You've found all these MACMAC's in the area!")
    print(deviceList)


    deviceString = ""
    for devices in deviceList:
        deviceString = deviceString+str(devices)

#    subprocess.call(['sudo','python2','write_minishift.py',deviceString])

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

#    subprocess.call(['sudo','python2','write_minishift.py',+str(pickedDevice)+" is close enough to catch!    Catch it?"])
    print("Pick?")


    #Pick or decline

    picked = None

    while(gpio.input(23) == 0 and gpio.input(24) == 1):

        if gpio.input(23) == 1:
            picked = True
        elif gpio.input(24) == 0:
            picked = False

    if picked == True:
        print ("You picked: "+str(pickedDevice))
#        subprocess.call(['sudo','python2','write_minishift.py',"You picked "+str(pickedDevice)+"!"])


    #checkForButtonYes()

    #Remove from deviceList

    deviceList.remove(pickedDevice)

    #add to pocket
    if picked == True:
        storedMonsters.append(pickedDevice)
        MacBank.write(str(pickedDevice)+"\n")



print ("You've gotL "+str(storedMonsters))

#Connect to server
sock = socket.socket()
host = "localhost"
port = 1337

sock.connect((host,port))

print ("Pick a MACMonster to send to FIGHT")
pickedDevice = None
for device in storedMonsters:

    print(device)

    while(gpio.input(23) == 0 and gpio.input(24) == 1):

        if gpio.input(23) == 1:
            pickedDevice = device
        elif gpio.input(24) == 0:
            pickedDevice = device

sock.send(str(pickedDevice).encode())

#Check if other people connected
#Send MAC address
#Wait until we're told we've won


