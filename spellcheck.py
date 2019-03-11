#program to identify spelling mistakes in sentences
f = open("words.txt", "r")
sent = open("para.txt", "r")
word = sent.readline()
print "mispelled words are:"
while word:
	word = word.lower()
	success = False
	x = word.split()
	y=len(x) 
	for i in x:
		success = False
		f = open("words.txt", "r")
		line = f.readline()
		while line:
    			if i == line.strip(): 
        			success = True
        			break
    			line = f.readline()
		f.close()   
		if success == False: 
			print i
	word = sent.readline()
sent.close()
	



