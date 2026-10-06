bringcharger = False
battery = None
timeleft = None
inputloop = True

while inputloop == True:
    try:
        battery = int(input("Enter remaining battery: "))
        timeleft = int(input("Enter how long you wish to remain in library: "))
        inputloop = False
        #if the user has entered valid numbers, the loop will end
    except ValueError:
        print("Please enter a valid number")
        #if the user enters a non integer, an error will occur
        #and ask them for input again


#2 mins per battery percentage
if (timeleft * 2) > battery:
    bringcharger = True
    print("You should bring your charger!")
else:
    print("You can leave your charger at home")