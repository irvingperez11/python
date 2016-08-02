import math
answer = "The Total amount time is "


vi = float(raw_input("enter initial velocity: "))
a = 9.81 
vf = 0
t = (vf-vi)/(a*-1)
t = t* 2

print answer + str(round(t,1)) + "s" 
#print vf

#print round(vf-vi/a)*-2