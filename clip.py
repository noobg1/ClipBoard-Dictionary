import time
import sys
import os
import pyperclip
import json
from PyDictionary import PyDictionary
from pprint import pprint
from easygui import *
import Tkinter
from sound import play
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from textblob import Word
from offlineDictionary import offline_meaning
from file_write import write_to_file

executor = ThreadPoolExecutor(2)

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
        continue_to_play = True
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
	    	
	    		
                choices = ["Continue","Stop Service", "Pronunciation", "Mark"]
                
                while(continue_to_play):
                    reply=buttonbox(msg,title="simple gui",choices=choices)
                    print reply
                    if reply == 'Stop Service': 
                        continue_check = False
                        continue_to_play = False
                    elif reply == 'Pronunciation':
                        executor.submit(play,recent_value)
                    elif reply == 'Continue':
                        continue_to_play = False
                    elif reply == 'Mark':
                        write_to_file(msg)
        
        except Exception as e:
                result = '#' + recent_value + '\n\n' + offline_meaning(recent_value) + '\n\n ~ offline'
                choices = ["Continue","Stop Service", "Pronunciation"]
                while(continue_to_play):
                    reply=buttonbox(result,title="simple gui",choices=choices)
                    print reply
                    if reply == 'Stop Service': 
                        continue_check = False
                        continue_to_play = False
                    elif reply == 'Pronunciation':
                        executor.submit(play,recent_value)
                    elif reply == 'Continue':
                        continue_to_play = False
                    elif reply == 'Mark':
                        write_to_file(msg)
                            
                msgbox("Value not found or check internet connection", title="simple gui")
    time.sleep(0.1)

sys.exit(0) 
			
			
			
			
			
			