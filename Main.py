import Biodiversity
"""Importing the given Biodiversity file which imports math so i dont need to
this file defines the two functions Calculate distance and Line to List."""

Newlist = []
#must be defined outside of the function as is a global variable

#-----------Added function to make the code better------------#
def OpenAndSortFile (FileName):
    file = open(FileName, "r")
    lines = []
    for line in file:
        lines.append(line)   
    file.close()
    #Opened file is reads in line by line using a loop adding each line as an item of a list (lines).
    
    for x in lines:
        Newlist.append (Biodiversity.LineToList(x))
    """Uses the line to list function given to pass each of these lines in the list
    just created and split them into three elements this creates a 2d array.
    All the species names being Newlist[x][0] all the latitudes being Newlist[x][1] etc."""

    return Newlist

#----------PART 1----------#

def LocationCount (FileName, Distanceinkm, Lat, Long):
    
    Num1 = 0
    #variable defined to be used as a counter

    OpenAndSortFile(FileName)
    
    for loop in range(0, len(Newlist)):
        nD= Biodiversity.CalculateDistance(Lat, Long, Newlist[loop][1], Newlist[loop][2])
        if nD <= Distanceinkm :
            Num1 += 1

    """Calculates the distance from a given location to all the locations in the file. 
    I used a loop so it runs through all the locations of all the animals in the array 
    returning their distances from the location as nD. The nD is compared to the Distanceinkm
    and if its less than or equal to it then the Number variable increases which is a running 
    count of the number of animals in the range. """

    return Num1

#----------PART 2----------#

def PrintLocation(FileName, Distanceinkm, Lat, Long):
    
    OpenAndSortFile(FileName)
        
    f = open("output.kml", "w")
    f.write('<Document> \n')
    x = ', '
    for loop in range(0, len(Newlist)):
        nD= Biodiversity.CalculateDistance(Lat, Long, Newlist[loop][1], Newlist[loop][2])
        if nD <= Distanceinkm :
            f.write ('<Placemark> \n')
            f.write ('<description>')
            f.write (Newlist[loop][0])
            f.write ('</description> \n')
            f.write ('<Point> \n')
            f.write ('<coordinates>')
            f.write (Newlist[loop][2])
            f.write (x)
            f.write (Newlist[loop][1])
            f.write ('</coordinates> \n')
            f.write ('</Point> \n')
            f.write ('</Placemark> \n')
    f.write('</Document>')
    f.close()
      
    """File opened called output.kml in write mode. If a file called output.kml is present it
    clears and rewrites that if not it creates one. Then the kml file is writen using the correct 
    format shown in the handbook. A loop is used to search through the list using the lat and long 
    values to find the sightinings within the desired range. If in the correct range the species name
    and coordiates are added to the kml file in the correct format."""
    
#----------PART 3----------#        
    
def BiodiversityCount (FileName, Distanceinkm, Lat, Long):
    
    Num2 = 0
    
    OpenAndSortFile(FileName)
    
    ListofSpecies = []
    for loop in range(0, len(Newlist)):
        nD= Biodiversity.CalculateDistance(Lat, Long, Newlist[loop][1], Newlist[loop][2])
        if nD <= Distanceinkm :
            ListofSpecies.append(Newlist[loop][0])
    ListofSpecies=set(ListofSpecies)
    Num2 = len(ListofSpecies)
    return Num2

    #This code creates a new list called ListofSpecies, then a loop is used to search through
    #Newlist and all the sightings which happen within the specified range are appended to the
    #ListofSpecies, the species names are added only.
    #Then line 113 removes any duplicate species names so the lis is of all the different
    #species that have been sighted in this area then the length of this list is returned.

#----------MAIN----------#

#PART 1
print("The Number of animals within the given distance from the given location is")
print(LocationCount ("Mammal.txt", 10.0, 54.988056, -1.619444))

"""This function is called using the data in the assignment sheet. As the function is printed
and the return from the function is the Number variable which is the total number of animals
in the range."""

#PART 2
PrintLocation ("Mammal.txt", 15.0, 51.452884, -0.973906)

"""Calling upon this function creates a kml file using the data from the mammal.txt file and
including data point wihtin 15km of the location the coordinates are provided for."""

#FIn = open("output.kml", "r")  
#for Line in FIn:
#    Line = Line.rstrip()
#    print(Line) 
#FIn.close()
#This section of commented code if uncommented would read the output.kml file just created
#and print it to the screen i used this in part of my testing stage as well as looking at
#the actual kml files created when the code is run.

#PART 3
print("The Number of species within the given distance from the given location is")
print(BiodiversityCount ("Mammal.txt", 25.0, 51.508129, -0.128005))

"""This function is called in a print function so the return from the function is printed.
In this case the retrun of BiodiversityCount is how many different species are found
within the area specified when the function is called."""