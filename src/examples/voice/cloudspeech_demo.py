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

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient

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
                    number = i
            if showString in text:
                print(number)
            
if __name__ == '__main__':
    main()

