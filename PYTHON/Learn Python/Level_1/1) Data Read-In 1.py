########
#Data Reading
########

#Python is capable of handling files well
#Reading files is pretty easy.

f = open('Sample_1.txt')#There can be more arguments than we have here
#######################But for now we have opened Sample in read mode
#######################Sample is in the same folder as this program

print f.readline() #This will print the first line in the file
print f.readline() #this will print the second line in the file
####################It prints the second line b/c it starts where it
####################left off.
print f.read() #this will read the rest of the file


#When you run this you will notice the gaps between lines, this is
#because there is a new line read in the file, as well as a new line
#printed as part of python.
