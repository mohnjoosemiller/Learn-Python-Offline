####
#defining functions
####

#Everything that has been covered so far has been the product
#of loops, and various other definitions. for real fun we begin
#to involve functions that can be called.

#functions are based on multiple variables that are separated
#by commas

def f (a, L=[]):
    L.append(a**2)
    return L ###Return is another way to output the list

f(1)
f(3)
f(5)
print(f(6))

