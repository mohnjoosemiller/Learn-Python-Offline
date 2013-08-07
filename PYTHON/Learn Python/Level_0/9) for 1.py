####
#'for' loops
####

#We have already learned 'while' loops but for
#many things 'for' loops will be a better fit

print('First loop\n')
for x in range(10): #What we are saying here is
    #################for a certaing range of x
    #################values do something
    print(x)#Here our output is simply x to show
    #########how the for loop works
print ('\n\n Second loop \n')
for x in range(1, 10):
    print (x)
print ('\n\n','Third loop \n')
for x in range(1, 20, 2):
    print ('x =', x) #just to give a little flavour
    ################I've added some formating
    pass

#Run this program and pull the results up so you
#Can see them and this.

#As you can see there different ways a for loop
#can work

#First way:
#in the range() if the only argument (that's what
#the things within '()' are called) is a single
#number it will start at zero and run through to
#that number but wil not include it. because I
#am running it with 10 it prints the first ten
#numbers starting from 0

#Second way:
#Running range() with two arguments yeilds a
#starting value, and an upper bound that won't be
#included. range(1, 10) yeilds an output of 1-9

#Third way:
#range() with three arguments is the same as the
#second loop but the third value is the step.
#This means what your change in x from one loop to
#the next. range(1, 20, 2) yields odd numbers
#starting from 1, to 20. (AKA every other number
#1-20)
