#Reading executing files 
#1. Read
#listofNames = open("names.txt")

#print(type(listofNames))
#print(listofNames.read())

#2. 
#for name in listofNames:
#    print(name)

#listofNames.close()

#3
listofNames = open("names.txt", "a")
listofNames.write("Larry Warry")
listofNames.close()
