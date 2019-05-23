#pi Zero WH
#python

import RPi.GPIO as GPIO

#pi light pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

#inc and dec buttons
input_inc = GPIO.input(31)
input_dec = GPIO.input(33)
if input_inc == False: 
    number = number + 1 #increase number for 8 bit
if input_dec == False:
    number = number - 1 #decrease number for 8 bit

#i'm not sure if this code works...
if div >= 2**8:
    #if error exists
    n = 0 #first while loop b/c pins light up twice
    x = 0 #second while loop to turn on lights and then turn off
    while n < 2:
        while x < 8:
            GPIO.output(pin[x], GPIO.HIGH) #turn all lights on
            x = x + 1
        x = 8
        while x < 8:
            GPIO.output(pin[x], GPIO.LOW) #turn all lights off
        n = n + 1

#potential pins
#NA pin = [3, 8, 11, 15, 18, 19, 23, 26]

x = 0 #counting up for array location
n = 7 #count down for base 2
#div = 95    testing number
light = [0,0,0,0,0,0,0,0] #empty binary array
pin = [7,11,13,15,18,22,32,36] #pin location

while x < 8: #going through binary digits
    max = 2 ** (n) #binary base-2
    #print (max)
    if number >= max: #if divisible
        number = number % max #then save the remainder
        light[x] = 1
        GPIO.output(pin[x], GPIO.HIGH) #if this bit is 1, light will light
    else:
        light[x] = 0
        GPIO.output(pin[x], GPIO.LOW) #if this bit is 0, light wont light
    x = x + 1
    n = n - 1
print (light)
