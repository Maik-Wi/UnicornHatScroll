#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script shows the current time

from UHScroll import *
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime('%H:%M')
unicorn_scroll(current_time,'white',160,0.15)
