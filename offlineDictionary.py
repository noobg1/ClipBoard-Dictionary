from nltk.corpus import wordnet

def offline_meaning(word):
	try:
		syns = wordnet.synsets(word)
		return syns[0].definition()
	except:
		return 'Not in offline repository'