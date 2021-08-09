# Import the os library
import os
# create input variables: prompt the user to input the directory address, file to be created, his/her full legal name, his/her address, his/her phone number
nameOfDirctry = input("Enter Directory Address to store the new file: ")
nameOfFileToBeMade = input("Please enter the name of file to be created: ")
inputName = input("Please enter your legal full name: ")
inputAddr = input("Please enter your full address: ")
inputContactNum = input("Please enter your phone number.: ")
# Determine if the name of directory entered by user is there
if os.path.isdir(nameOfDirctry):
    # create new file 
    fileToBeWrittenTo = open(os.path.join(nameOfDirctry, nameOfFileToBeMade), "w")
    # variable for new file
    fileToBeWrittenTo.write(inputName + str(",") + inputAddr + str(",") + inputContactNum)
    fileToBeWrittenTo.close()
    #print statement
    print("The data in file is: ")
   # open file in read mode 
    fileToBeScanned = open(os.path.join(nameOfDirctry, nameOfFileToBeMade), "r")
    # Read file and print 
    print(fileToBeScanned.read())
    fileToBeScanned.close()
# Otherwise print the error
else: 
    print("The directory mentioned is non-existent, please try again!")