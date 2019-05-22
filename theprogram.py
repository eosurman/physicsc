import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

number = 0 #default number

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    for i in range(256):
        toString = str(i)
        recognizer.expect_phrase('Set '+toString)
        recognizer.expect_phrase('Add '+toString)
        recognizer.expect_phrase('Subtract ' + toString)

    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if not text:
            print('Sorry, I did not hear you.')
        else:
            for i in range(256):
                toString = str(i)
				if 'Set '+toString in text:
                    number = i
				if 'Add '+toString in text:
                    number += i
                if 'Subtract '+toString in text:
                    number -= i
                if number > 255
                    number = 255
				elif number < 0
                    number = 0
        print number

if __name__ == '__main__':
    main()