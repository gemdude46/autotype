
from setuptools import setup

setup(
	name='autotype',
	version='1.0.0',
	description='A Unicode-friendly tool for faking key presses to type strings on X11.',
	url='https://github.com/gemdude46/autotype',
	author='Marley Adair (gemdude46)',
	keywords='x x11 xautomation automation',
	packages=['autotype'],
	install_requires=['python3-xlib'],
	python_requires='>=3,<4'
)
