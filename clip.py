import time
import sys
import os
import pyperclip
import json
from PyDictionary import PyDictionary
from pprint import pprint
from easygui import *
import Tkinter

dictionary=PyDictionary()
window = Tkinter.Tk()
window.wm_withdraw()
sys.path.append(os.path.abspath("SO_site-packages"))


recent_value = ""
start = True
continue_check = True
pyperclip.copy('') 

while continue_check:
    tmp_value = pyperclip.paste()
    
    if start:
        msgbox("Service Started", title="simple gui") 
        start = False

    elif tmp_value != recent_value:
        recent_value = tmp_value
        print "Value changed: %s" % str(recent_value)[:20]
        try:
	        result = dictionary.meaning(str(recent_value))
	        for key, value in result.items():
	    		print value
	    		msg = "# " + recent_value
                msg += "\n\n" + "# " + key + "\n\n"
                for v in value[:5]:
	    			msg += ". " + v + ".\n"
	    		
                print msg
	    		
                choices = ["Continue","Stop Service"]
                
                reply=buttonbox(msg,title="simple gui",choices=choices)
                print reply
                if reply == 'Stop Service': 
                    continue_check = False
        except Exception as e:
    		print e           
    		msgbox("Value not found or check internet connection", title="simple gui")
    time.sleep(0.1)

sys.exit(0) 