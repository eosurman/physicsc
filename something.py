#pi Zero WH
#python
#import math

#if div >= 2**8:
    #error
#    e = 0
#    x = 0
#    while e < 2
#        while x < 8
#            GPIO.output(light[x][2], GPIO.HIGH)
#            x = x + 1
#        while x < 8
#            GPIO.output(light[x][2], GPIO.LOW)
#        e = e + 1

#potential pins
#pin = [3, 8, 11, 15, 18, 19, 23, 26]

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.3)
#GPIO.setmode(GPIO.10)
#GPIO.setmode(GPIO.9)
#GPIO.setmode(GPIO.11)
#GPIO.setmode(GPIO.14)
#GPIO.setmode(GPIO.15)
#GPIO.setmode(GPIO.7)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)



x = 0 #counting up for array location
n = 7 #count down for base 2
number = 32   # number
light = [0,0,0,0,0,0,0,0]
pin = [3, 5, 19, 21, 23, 8, 10, 26]

while x < 8: #going through binary digits
    max = 2 ** (n) #binary base-2
    #print (max)
    if number >= max: #if divisible
        number = number % max #then save the remainder
        light[x] = 1
        GPIO.output(pin[x], GPIO.HIGH)
    else:
        light[x] = 0
        GPIO.output(pin[x], GPIO.LOW)
    x = x + 1
    n = n - 1
print (light)
