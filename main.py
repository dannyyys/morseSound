from sound import sound
from convert import convert

while True:
    try:
        print('~~~~Menu~~~~')
        print('1: Text to morse code')
        print('2: Exit')
        selection = int(input('Select Your Choice: '))
        if selection == 1:
            userText = input("Enter your message:")
            c = convert(userText)
            code = c.morseCode()
            print(code)
            print('Converting.. please wait.')
            m = sound(code)
            m.toSound()
            print('Finish converting!!')
            break
        elif selection == 2:
            print('Exiting')
            break
        else:
            print('Wrong Selection, enter again')
    except:
        print('Wrong Selection, enter again')