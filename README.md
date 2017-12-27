# Autotype
A Unicode-friendly tool for faking key presses to type strings on X11.

There are loads of tools for automating keyboard events and typing, like `xte`, as well as many language specific libraries, such as `pyautogui` and `java.awt.Robot`, however they all have one major flaw: They *completely* fuck up Unicode.

## Getting Started

### Prerequisites

Autotype requires python 3 and python xlib.

On Debian based systems, these can be installed with

```
apt install python3 python3-xlib
```

Xlib can also be installed with `pip`

```
pip3 install python3-xlib
```

### Installing

The python module can be installed using pip3:

```
pip3 install autotype
```

There is no support for python 2.

To install the command line tool, clone the repo with

```
git clone https://github.com/gemdude46/autotype.git
```

and run `install.sh`

## License

Autotype is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
