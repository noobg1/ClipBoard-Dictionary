import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))
import Tkinter
window = Tkinter.Tk()
window.wm_withdraw()

import pyperclip
import json
from PyDictionary import PyDictionary
dictionary=PyDictionary()

from pprint import pprint
import easygui







recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print "Value changed: %s" % str(recent_value)[:20]
        try:
	        result = dictionary.meaning(str(recent_value))
	        for key, value in result.items():
	    		print value
	    		msg = ""
	    		for v in value:
	    			msg += v + ".\n"
	    		print msg
	    		easygui.msgbox(msg, title="simple gui")
        except:
    		print "Value not found"
    		easygui.msgbox("Value not found", title="simple gui")
    time.sleep(0.1)