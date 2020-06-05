# ========  MORSE CODE
# Morse code was developed by SAMUEL MORSE and ALFRED VAIL.
# Program Developed by: KY
# Date: 5/6/2020

from playsound import playsound
def dot():
	''' It play dot sound '''
	playsound('dot.wav')
def dash():
	''' It play dash sound '''
	playsound('dash.wav')

morseCode = {
	'a': ".-", 
	'b': "-...",
	'c': "-.-.",
	'd': "-..",
	'e': ".",
	'f': "..-.",
	'g': "--.",
	'h': "....",
	'i': "..",
	'j': ".---",
	'k': "-.-",
	'l': ".-..",
	'm': "--",
	'n': "-.",
	'o': "---",
	'p': ".--.",
	'q': "--.-",
	'r': ".-.",
	's': "...",
	't': "-",
	'u': "..-",
	'v': "...-",
	'w': ".--",
	'x': "-..-",
	'y': "-.--",
	'z': "--..",
	'1': ".----",
	'2': "..---",
	'3': "...--",
	'4': "....-",
	'5': ".....",
	'6': "_....",
	'7': "--...",
	'8': "---..",
	'9': "----.",
	'0': "-----",
	' ': "",
	}
	
def player(code):
	''' 
	morse Code player 
	Parameter: Code
	Method name: Player
	'''
	for i in code:
		if i == '.':
			dot()
		if i == '-':
			dash()
	
print("======= Text to Morse Code Converter ========")
text = str(input("Enter text: "))
print("Character : Morse code")
for i in text:
	print(i,"\t:\t",morseCode[i.lower()])
	player(morseCode[i.lower()])