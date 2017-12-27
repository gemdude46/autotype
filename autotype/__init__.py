import os
import subprocess
import time

from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input

_display = Display(os.environ['DISPLAY'])

def type(text, delay=0.03, down_for=0):
	'''Fake key presses to type out text.
	
	Args:
	  text (str): The text to type out.
	  delay (float): The time to wait between presses. (In seconds)
	  down_for (float): How long to keep each key down. (In seconds)
	
	Returns:
	  None
	'''
	
	# Save the users existing keyboard mapping
	kbm_backup = _display.get_keyboard_mapping(8,246)

	try:
		
		text = text.replace('\n', '\r') # Because X

		# Splits the text into blocks containing no more than 245 unique characters
		# This is because there is a limited number of valid xmodmap keycodes
		while text:
			chars = set()

			i = 0
			while i < len(text) and len(chars) < 245:
				char = ord(text[i])
				chars.add(char)
				i += 1

			block = text[:i]
			text = text[i:]

			_type_lt245(block, delay, down_for)
	
	finally:

		# Restore the keyboard layout to how it was originally
		_display.change_keyboard_mapping(8, kbm_backup)
		_display.sync()

def _type_lt245(text, delay, down_for):
	
	xmm = ''
	
	chars = []

	keys = []

	text = [(1 << 24) + ord(i) for i in text]

	for char in text:
		if char not in chars:
			chars.append(char)
		
		keys.append(chars.index(char) + 8)
	
	for i in range(8, 255):
		fake_input(_display, X.KeyRelease, i)

	_display.change_keyboard_mapping(8, [(i, ) * 15 for i in chars])
	_display.sync()

	for key in keys:

		fake_input(_display, X.KeyPress, key)
		_display.sync()

		time.sleep(down_for)

		fake_input(_display, X.KeyRelease, key)
		_display.sync()

		time.sleep(delay)

