def f (a, L=[]):
    L.append(a**2)
    return L ###Return allows the function to read the appended
            ####list

x = -10
while x < 10 :
    f(x)
    x += .1
print (f(10))
