####
#Data Read-In 2
####

#often we want to control exactly what we read from
#a file. Here we learn a tad more about reading

#Loops come in handy especially when dealling with
#longer files

#An example:

f = open('Sample_1.txt', 'r')#last time we didn't include a
##############################second argument, 'r' tells Pyhton
##############################to open a file in read-only mode

x=0
for x in range(1, 9):
    print f.readline()
    x += 1
    
