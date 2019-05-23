import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT, initial=0)
GPIO.setup(11, GPIO.OUT, initial=0)
GPIO.setup(13, GPIO.OUT, initial=0)
GPIO.setup(15, GPIO.OUT, initial=0)
GPIO.setup(18, GPIO.OUT, initial=0)
GPIO.setup(22, GPIO.OUT, initial=0)
GPIO.setup(32, GPIO.OUT, initial=0)
GPIO.setup(36, GPIO.OUT, initial=0)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if input_inc == False: 
    #number = number + 1 #increase number for 8 bit
if input_dec == False:
    #number = number - 1 #decrease number for 8 bit
if number >= 2**8:
            #if error exists
    n = 0 #first while loop b/c pins light up twice
    x = 0 #second while loop to turn on lights and then turn off
    while n < 2:
        while x < 8:
            GPIO.output(pin[x], 1) #turn all lights on
            x = x + 1
        x = 8
        while x < 8:
            GPIO.output(pin[x], 0) #turn all lights off
            n = n + 1
#potential pins
#NA pin = [3, 8, 11, 15, 18, 19, 23, 26]
#pin = [3, 5, 19, 21, 23, 8, 10, 26] #pin location                  
x = 0 #counting up for array location
n = 7 #count down for base 2
#div = 95    testing number
light = [0,0,0,0,0,0,0,0] #empty binary array
pin = [7, 11, 13, 15, 18, 22, 32, 36] #pin location
while x < 8: #going through binary digits
    max = 2 ** (n) #binary base-2
    #print (max)
    if number >= max: #if divisible
        number = number % max #then save the remainder
        light[x] = 1
        GPIO.output(pin[x], 1) #if this bit is 1, light will light
    else:
        light[x] = 0
        GPIO.output(pin[x], 0) #if this bit is 0, light wont light
    x = x + 1
    n = n - 1
print (light)
