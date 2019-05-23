#pi Zero WH
#python
#import math

if div >= 2**8:
    #error
    e = 0
    x = 0
    while e < 2
        while x < 8
            GPIO.output(light[x][2], GPIO.HIGH)
            x = x + 1
        while x < 8
            GPIO.output(light[x][2], GPIO.LOW)
        e = e + 1

#potential pins
#pin = [3, 8, 11, 15, 18, 19, 23, 26]

x = 0 #counting up for array location
n = 7 #count down for base 2
#div = 95    number
light[8][2] = [0,0,0,0,0,0,0,0], [3, 5, 19, 21, 23, 8, 10, 26]

while x < 8: #going through binary digits
    max = 2 ** (n) #binary base-2
    #print (max)
    if number >= max: #if divisible
        number = number % max #then save the remainder
        light[x][1] = 1
        GPIO.output(light[x][2], GPIO.HIGH)
    else:
        light[x][1] = 0
        GPIO.output(light[x][2], GPIO.LOW)
    x = x + 1
    n = n - 1
print (light)
