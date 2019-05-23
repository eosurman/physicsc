import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
 
number=0
def main():
 recognizer = aiy.cloudspeech.get_recognizer()
 recognizer.expect_phrase('The number is 1.')
 recognizer.expect_phrase('The number is 2.')
 recognizer.expect_phrase('The number is 3.')
 recognizer.expect_phrase('What is the number?')


aiy.audio.get_recorder().start()
 
while True:
 print('Press the button and speak')
 button.wait_for_press()
 print('Listening...')
 text = recognizer.recognize()
 if not text:
  print('Sorry, I did not hear you.')
  else:
    print('You said "', text, '"')
     if 'The number is 1.' in text:
      number = 1
     elif 'The number is 2.' in text:
      number = 2
     elif 'The number is 3.' in text:
      number = 3
     elif 'goodbye' in text
      print('The number is "'number '"')
      break
 
 
if __name__ == '__main__':
 main()
 
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
x = 0 #counting up for array location
n = 7 #count down for base 2
number = 50   # number
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

