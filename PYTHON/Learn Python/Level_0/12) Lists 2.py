####
#Lists 2
####

#undoubtably you will be wanting to add data to lists without manually
#inputing the values, thankfully lists have a few different ways they
#can be altered.

x = 1 #creating some variables that we can add to the list
y = 2
z = 3

a = ['a', 'b', 'c'] #our starting list
print(a) #our initial output

#Now we want to start adding to our list
#First we will add x to the end using append
a.append(x)
print(a)

#Now we will add y at the beginning of the list
a.insert(0,y) #Remember that 0 is the first position in Computer
              #Science

#And z to the third position
a.insert(2,z) # we use 2 to represent the third position because
            ### in Computer science counting starts from 0
print(a)
