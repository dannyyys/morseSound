from MorseCode import MorseCode

while True:
    print('~~~~Menu~~~~')
    print('1: Text to morse code')
    print('2: Exit')
    menu_selection = int(input('Enter your choice: '))

    if menu_selection == 1:
        english_text = str(input('Enter english text: '))
        morseCode = MorseCode(english_text)

        print(morseCode.code)
    else:
        break