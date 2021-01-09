class MorseCode:
    """This class allow user to instantiate MorseCode object with english text
    and convert given english text into morseCode and morseCodeSound

    morseCode could be obtained from MorseCode object with MorseCode.code
    morseCodeSound could be obtained from MorseCode object with MorseCode.sound
    """

    # To convert english alphabets to morseCode
    MORSE_CODE_DICT = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ', ': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '/': '-..-.',
        '-': '-....-',
        '(': '-.--.',
        ')': '-.--.-'
    }

    def __init__(self, english_text):
        """Upon instantiation, converts given english_text to
        morseCode and morseCodeSound

        Args:
            english_text (str): Text in english to convert to 
            morseCode or to morseCodeSound
        """
        self._english_text = english_text
        self.code = self._to_morse_code()
        self.sound = self._to_morse_code_sound()

    def _to_morse_code(self):
        """Convert self._english_text to morse code

        Returns:
            str: morse code representation in string 
        """
        code = [
            MorseCode.MORSE_CODE_DICT[i.upper()] + ' '
            for i in self._english_text
            if i.upper() in MorseCode.MORSE_CODE_DICT.keys()
        ]

        return ''.join(code)

    def _to_morse_code_sound(self):
        """Convert self._english_text to morse code sound

        Returns:
            str: absolute path to output.wav file that contains 
            morse code representation in sound format  
        """
        sound = None

        return f'{self._english_text} converted to morseCodeSound'