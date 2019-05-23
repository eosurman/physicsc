#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# AP Physics C Lightbulb Project

import argparse
import locale
import logging
import RPi.GPIO as GPIO
import time

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
"""
GPIO.setmode(GPIO.BCM)
            #GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            #GPIO.setup(12, GP
            #IO.IN, pull_up_down=GPIO.PUD_UP)
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
"""
# Defining variables
number = 0
bucketAmt = 256
stringBucket = []
setString = 'set counter '
showString = 'show counter'

# Pre set all the text that it can detect. This limits the set number to be limited to 256
def get_hints(language_code):
    if language_code.startswith('en_'):
        for i in range(bucketAmt): 
            toString = str(i)
            stringBucket.append(setString+toString)
        return stringBucket
    return None

# Internalized
def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

# Magic Code
def main():
    logging.basicConfig(level=logging.DEBUG)


    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            if hints:
                #logging.info('Say something, e.g. %s.' % ', '.join(hints))
                logging.info('say something')
            else:
                logging.info('Say something.')
            text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
            if text is None:
                logging.info('You said nothing.')
                continue

            logging.info('You said: "%s"' % text)
            text = text.lower()
            
# Using for-loop, the program gives out only the resulting number
            for i in range(bucketAmt):
                toString = str(i)
                if setString+toString in text:
                    numer = i
            if showString in text:
                print(number)
##                break
            #pi Zero WH
            #python

            #pi light pin setups
            #GPIO.setmode(GPIO.BOARD)


            #inc and dec buttons
            #while True:
                #input_state = GPIO.input(31)
                #if input_state == False:
                    #number = number + 1
                    #time.sleep(0.2)
                
            
            #while True:
                #input_state = GPIO.input(33)
                #if input_state == False:
                    #number = number - 1
                    #time.sleep(0.2)
                
            """
            #input_inc = GPIO.input(11)
            #input_dec = GPIO.input(12)
#if input_inc == False: 
    #number = number + 1 #increase number for 8 bit
#if input_dec == False:
    #number = number - 1 #decrease number for 8 bit
#div = number

            #i'm not sure if this code works...
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
"""

            
if __name__ == '__main__':
    main()
