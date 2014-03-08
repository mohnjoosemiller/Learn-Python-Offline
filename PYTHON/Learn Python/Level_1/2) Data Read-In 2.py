####
#Data Read-In 2
####

#often we want to control exactly what we read from
#a file. Here we learn a tad more about reading

#Loops come in handy especially when dealing with
#longer files

#An example:

f = open('Sample_2.txt', 'r')#last time we didn't include a
##############################second argument, 'r' tells Python
##############################to open a file in read-only mode

for x in range(1, 9):
    print f.readline()#reads the line that the 
    x += 1 #to advance to the next value
    
