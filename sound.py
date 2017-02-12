import pyttsx
def onStart(name):
   print 'starting', name
def onWord(name, location, length):
   print 'word', name, location, length
def onEnd(name, completed):
   sys.exit()
   print 'finishing', name, completed

def play(word):
	engine = pyttsx.init()
	engine.connect('started-utterance', onStart)
	engine.connect('started-word', onWord)
	engine.connect('finished-utterance', onEnd)
	engine.say(word)
	engine.runAndWait()