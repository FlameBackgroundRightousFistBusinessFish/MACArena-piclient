import bluetooth
import random
import socket




MacBank = open("caught.txt", "w+")


storedMonsters = MacBank.readlines()

#Get all devices in the area
deviceList = bluetooth.discover_devices()

while (len(storedMonsters) < 3):


    #Display all the addresses
    print("You've found all these MACMAC's in the area!")
    print(deviceList)

    #for devices in deviceList()
    #minishift.scroll(deviceList)

    #Randomly pick one from the list
    rand = random.randint(0, len(deviceList)-1)

    
    print(rand)
    pickedDevice = deviceList[rand]
    

    #Show it to the user
    print("You've picked: ")
    print(pickedDevice)

    #minishift.scroll("You Picked!")
    #minishift.scroll(pickedDevice)

    #Pick or decline

    #checkForButtonYes()


    #Add to bank of addresses (a file?)

    #Remove from deviceList

    deviceList.remove(pickedDevice)

    #add to pocket
    storedMonsters.append(pickedDevice)
    MacBank.write(str(pickedDevice)+"\n")

#Repet until selected 3

#Connect to server
sock = socket.socket()
host = None
port = 1337

sock.connect((host,port))

#For all the devices we've collected, serialise them into a JSON packet

for device in storedMonsters: 
    writeString = writeString+"{\"MAC\":\""+str(device)+"\"},"

writeString = writeString[0:-1] #remove the trailing comma

sock.write("{\"deviceList\":"+writeString+"}")

#Check if other people connected
#Send MAC address
#Wait until we're told we've won
