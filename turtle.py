from turtle import *  #importerer turtlebiblioteket
import math   #importerer pylab for å bruke sqrt()

shape("turtle")
forward(30)         #tegner en strek
left(90)            #snur 90 grader mot høyre
forward(40)
left(143.13)
dist = math.sqrt(40**2 + 30**2)  #pytagoras for å regne ut avstand til start
forward(dist)

print(pos()) #skriver ut posisjonen du har på skjermen
