Unicorn Hat Scrolling text
==========================

This Python provides a simple way to generate a scrolling text message on a [Pimoroni Unicorn Hat] (http://shop.pimoroni.com/products/unicorn-hat). To see some examples, have a look at my [blog] (http://richardhayler.blogspot.com/2014/12/unicorn-hat-text-scroller.html)

Requirements
------------

[unicornhat] (https://github.com/pimoroni/UnicornHat)

bitarray

Installation
------------

pip install unicornhat

pip install bitarray

git clone https://github.com/topshed/UnicornHatScroll

Files
-----

**UHScroll.py**

The main file which defines all the functions 

**UHScroll_defs.py**

Contains all the character designs and mappings

**test.py**

A simple test program 

**imap.py**

This script displays your unread emails.

**time.py**

This script displays the current time.

**btc.py**

This script shows the current bitcoin rate in Euro. 

**btc-ticker.py**

This script repeatedly displays the current bitcoin price. 


Usage
-----

```python
from UHScroll import *

unicorn_scroll(text,colour,brightness,speed)
```

*example:*
 
```python
unicorn_scroll('hello world','red',255,0.1)
```
Special Symbols
---------------

There are 6 special (non-keyboard) symbols available. These are used by prefixing their 5 character name with a tilde (~).

- For a smile use ~smilie
- For a heart use (you guessed it) ~heart
- For a degrees use ~degrs (for best results, don't leave a space between the preceeding number and the symbol)
- For a heart use letter use ~email
- For a euro use ~euros
- For a euro bitcon use ~bcoin


*example:*

```python
unicorn_scroll('I ~heart unicorns','pink',255,0.1)
unicorn_scroll('It is 25~degrsc','blue',255,0.5)
