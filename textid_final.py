#Jenny(Yuqing) Cang, Grace Stewart, and Umar Farooq
#Final woo!



from porter import create_stem
import math

class TextModel:

	def __init__(self, name):
		""" the constructor for the TextModel class
			all dictionaries are started at empty
			the name is just for our own purposes, to keep things 
			organized
		"""
		self.name = name
		self.words = {}   # starts empty
		self.wordlengths = {}
		self.stems = {}
		self.sentencelengths = {}
		self.punc = {}
		# you will want another dictionary for your text feature


	def __repr__(self):
		""" this method creates the string version of TextModel objects
		"""
		s  = "\nModel name: " + str(self.name) + "\n"
		s += "    n. of words: " + str(len(self.words))  + "\n"
		s += "    n. of word lengths: " + str(len(self.wordlengths))  + "\n"
		s += "    n. of sentence lengths: " + str(len(self.sentencelengths))  + "\n"
		s += "    n. of stems: " + str(len(self.stems))  + "\n"
		# you will likely want another line for your custom text-feature!
		return s

	def readTextFromFile(self,filename):
		"""This method should take in a filename (a string) and should return all of the text in that file as a single, possibly very large string
		"""
		f=open(filename)
		text=f.read()
		f.close()
		return text

	def makeSentenceLengths(self,s):
		""" should use the text in the input string s to create the self.sentencelengths dictionary
		"""
		self.sentencelengths = {}
		s = s.split()
		sentleng = 0
		
		for word in s:
			sentleng += 1
			if "." in word or '!' in word or '?' in word:
				if sentleng not in self.sentencelengths:
					self.sentencelengths[sentleng] = 0
				self.sentencelengths[sentleng] += 1
				sentleng = 0

	def cleanString(self,s):
		"""returns a string with no punctuation and no upper-case letters"""
		s = s.lower()
		s = s.split()

		for i in range(len(s)):
			if "." in s[i] or '!' in s[i] or '?' in s[i] or ';' in s[i] or ':' in s[i] or ',' in s[i]:
				s[i] = s[i][:-1]
			if "'" in s[i] or "-" in s[i] or "_" in s[i] or '(' in s[i] or ')' in s[i] or '[' in s[i] or ']' in s[i] or '"'in s[i]:
				s[i] = s[i].replace("'","")
				s[i] = s[i].replace("-","")
				s[i] = s[i].replace(")","")
				s[i] = s[i].replace("(","")
				s[i] = s[i].replace("_","")
				s[i] = s[i].replace("[","")
				s[i] = s[i].replace("]","")
				s[i] = s[i].replace('"',"")
			
		for i in range(len(s)):          
			s[i] = s[i] + ' '
		s = ''.join(s)
		return s


	def makeWordLengths(self,s):
		""" should use the text in the input string s to create the self.wordlengths dictionary"""
		
		s = self.cleanString(s)
		self.wordlengths = {}
		lengthword = 0

		for x in s:
			lengthword += 1
			if x == ' ':
				if lengthword not in self.wordlengths:
					self.wordlengths[lengthword] = 0
				self.wordlengths[lengthword] += 1
				lengthword = 0    
		
	def makeWords(self,s):
		""" should use the text in the input string s to create the self.words dictionary """
		s = self.cleanString(s)
		s = s.split()
		self.words = {}

		for word in s:
			if word not in self.words:
				self.words[word] = 0
			self.words[word] += 1
			
	def makeStems(self,s):
		""" should use the text in the input string s to create the self.stems dictionary """
		s = self.cleanString(s)
		s = s.split()
		self.stems = {}

		for word in s:
			word = create_stem(word)

		for word in s:
			if word not in self.stems:
				self.stems[word] = 0
			self.stems[word] += 1

	def makePunctuation(self,s):
		""" creates a dictionary of the punctuation frequency
		"""
		s = s.lower()
		self.punc = {}

		for char in s:
			if char in '!,?.-_':
				if char not in self.punc:
					self.punc[char] = 0
				self.punc[char] += 1

	def printAllDictionaries(self):
		"""prints all of the five self dictionaries"""

		print ('The text model named', [ self.name ], 'has dictionaries')
		print ('self.sentencelengths:', self.sentencelengths, '\n')
		print ('self.words:', self.words, '\n')
		print ('self.wordlengths:', self.wordlengths, '\n')
		print ("self.stems:", self.stems, '\n')
		print ("self.punc:", self.punc, '\n')

# put the text between these triple-quotes into a file named test.txt
# test_text = """This is a small sentence. This isn't a small sentence, because
# this sentence contains more than 10 words and a number! This isn't
# a question, is it?"""

# test_tm = TextModel( "Milestone test" )

# text = test_tm.readTextFromFile( "test.txt" )
# print("Is text == test_text? ", text == test_text)

# # create all of the dictionaries
# test_tm.makeSentenceLengths(text)
# test_tm.makeWordLengths(text)
# test_tm.makeWords(text)
# test_tm.makePunctuation(text)
# test_tm.makeStems(text)

# # first, let's see test_tm via the __repr__ method
# print(test_tm)

# # next, let's see all of the dictionaries:
# test_tm.printAllDictionaries()

	def normalizeDictionary(self,d):
		""" takes in a single one of model-dictionaries, d, and returns a normalized version in which the values add up to 1
		"""
		newk = {}
		for k in d:
			sumvalue = sum(d.values())
			newk[k] = d[k]/sumvalue
		return newk

# test_tm = TextModel( "Final test" )
# d = {'a': 5, 'b':1, 'c':2}
# nd = test_tm.normalizeDictionary( d )
# print("The original dictionary is")
# print(d)
# print("The normalized dictionary is")
# print(nd)

	def smallestValue(self,nd1,nd2):
		""" takes in any 2 model dictionaries nd1 and nd2 and returns the smallest positive value across them both
		"""
		smallest1 = min(nd1.values())
		smallest2 = min(nd2.values())
		if smallest1 < smallest2:
			return smallest1
		else:
			return smallest2
		
# test_tm = TextModel( "Final test" )
# d1 = {'a': 5, 'b':1, 'c':2}
# nd1 = test_tm.normalizeDictionary( d1 )
# d2 = {'a': 15, 'd':1}
# nd2 = test_tm.normalizeDictionary( d2 )
# print("The normalized dictionaries are")
# print(nd1)
# print(nd2)
# sm_va = test_tm.smallestValue( nd1, nd2 )
# print("and the smallest value between them is", sm_va)


	def compareDictionaries(self,d,nd1,nd2):
		""" fundamental TextID method: computes the log-probability that d arose from data in nd1 and the log-probability that d arose from data in nd2
		"""
		total_log_prob1 = 0.0
		total_log_prob2 = 0.0

		epsilon = 0.5 * self.smallestValue(nd1,nd2)
		for k in d:
			if k in nd1:
				total_log_prob1 += d[k] * math.log(nd1[k])
			elif k not in nd1:
				total_log_prob1 += math.log(epsilon)

		for k in d:
			if k in nd2:
				total_log_prob2 += d[k] * math.log(nd2[k])
			elif k not in nd2:
				total_log_prob2 += math.log(epsilon)

		List_of_log_probs = [total_log_prob1,total_log_prob2]

		return List_of_log_probs



# test_tm = TextModel( "Final test" )
# d = {'a':2, 'b':1, 'c':1, 'd':1, 'e':1}
# print("The unnormalized dictionary is")
# print(d)
# print("\n")
# d1 = {'a': 5, 'b':1, 'c':2}
# nd1 = test_tm.normalizeDictionary( d1 )
# d2 = {'a': 15, 'd':1}
# nd2 = test_tm.normalizeDictionary( d2 )
# print("The normalized comparison dictionaries are")
# print(nd1)
# print(nd2)

# List_of_log_probs = test_tm.compareDictionaries(d, nd1, nd2)
# print("The list of log probs is")
# print(List_of_log_probs)


	def createAllDictionaries(self,s):
		""" creates all dictionaries with the input string s
		"""
		self.makeSentenceLengths(s)
		new_s = self.cleanString(s)
		self.makeWords(new_s)
		self.makeStems(new_s)
		self.makePunctuation(s)
		self.makeWordLengths(new_s)


	def compareTextWithTwoModels(self,model1,model2):
		""" runs the compareDictionaries method for all feature dictionaries in self against corresponding normalized dictionaries in model1 and model2
		"""
	
		a = self.normalizeDictionary(model1.words)
		b = self.normalizeDictionary(model2.words)
		L1 = self.compareDictionaries(self.words,a,b)
		
		c = self.normalizeDictionary(model1.wordlengths)
		d = self.normalizeDictionary(model2.wordlengths)
		L2 = self.compareDictionaries(self.wordlengths,c,d)

		e = self.normalizeDictionary(model1.sentencelengths)
		f = self.normalizeDictionary(model2.sentencelengths)
		L3 = self.compareDictionaries(self.sentencelengths,e,f)

		g = self.normalizeDictionary(model1.stems)
		h = self.normalizeDictionary(model2.stems)
		L4 = self.compareDictionaries(self.stems,g,h)

		i = self.normalizeDictionary(model1.punc)
		j = self.normalizeDictionary(model2.punc)
		L5 = self.compareDictionaries(self.punc,i,j)

		print("Overall comparison of",self.name, "vs", model1.name,'and',model2.name,': \n')

		print("{0:15} {1:<15} {2:<15}".format("name","vsTM1","vsTM2"))
		print("{0:15} {1:<15} {2:<15}".format("----","-----","-----"))
		print("{0:15} {1:<15.2f} {2:<15.2f}".format("words",L1[0],L1[1]))
		print("{0:15} {1:<15.2f} {2:<15.2f}".format("wordlengths",L2[0],L2[1]))
		print("{0:10} {1:<15.2f} {2:<15.2f}".format("sentencelengths",L3[0],L3[1]))
		print("{0:15} {1:<15.2f} {2:<15.2f}".format("stems",L4[0],L4[1]))
		print("{0:15} {1:<15.2f} {2:<15.2f}".format("punctuation",L5[0],L5[1]))

		model1wins = 0
		model2wins = 0

		if L1[0] > L1[1]:
			model1wins += 1
		else: 
			model2wins +=1

		if L2[0] > L2[1]:
			model1wins += 1
		else: 
			model2wins +=1		
		
		if L3[0] > L3[1]:
			model1wins += 1
		else: 
			model2wins +=1		
		
		if L4[0] > L4[1]:
			model1wins += 1
		else: 
			model2wins +=1

		if L5[0] > L5[1]:
			model1wins += 1
		else: 
			model2wins +=1
		
		print("\nModel1 - ",model1.name, "wins on", model1wins," features")
		print("Model2 - ",model2.name, "wins on", model2wins," features")
		if model1wins > model2wins:
			print("\n +++++      Model1 -", model1.name, "is the better match!      +++++\n")
		else:
			print("\n +++++      Model2 -", model2.name, "is the better match!      +++++\n")


print(" +++++++++++ Friends +++++++++++ ")
trained_tm1 = TextModel( "Friends" )
text1 = trained_tm1.readTextFromFile( "Friends.txt" )
trained_tm1.createAllDictionaries(text1)  # provided in hw description
# trained_tm1.printAllDictionaries()

print(" +++++++++++ Seinfeld +++++++++++ ")
trained_tm2 = TextModel( "Seinfeld" )
text2 = trained_tm2.readTextFromFile( "Seinfeld.txt" )
trained_tm2.createAllDictionaries(text2)  # provided in hw description
# trained_tm2.printAllDictionaries()

print(" +++++++++++ Test1 +++++++++++ ")
unknown_tm = TextModel( "Test1" )
text_unk = unknown_tm.readTextFromFile( "Test1.txt" )
unknown_tm.createAllDictionaries(text_unk)  # provided in hw description
# # unknown_tm.printAllDictionaries()

# print(" +++++++++++ Test2 +++++++++++ ")
# unknown_tm = TextModel( "Test2" )
# text_unk = unknown_tm.readTextFromFile( "Test2.txt" )
# unknown_tm.createAllDictionaries(text_unk)  # provided in hw description
# #unknown_tm.printAllDictionaries()

# print(" +++++++++++ Test3 +++++++++++ ")
# unknown_tm = TextModel( "Test3" )
# text_unk = unknown_tm.readTextFromFile( "Test3.txt" )
# unknown_tm.createAllDictionaries(text_unk)  # provided in hw description
# #unknown_tm.printAllDictionaries()

unknown_tm.compareTextWithTwoModels(trained_tm1,trained_tm2)

""" RESULTS
Our two models were based on scripts from Friends and Seinfeld, testing whether or not a random episode's script was more likely to be from Seinfeld or from Friends. Our model is relatively straightforward: whichever model has the most dictionaries match the text, that model wins. 

We found that our models mostly worked. Initially, they didn't work very well at all. We chose an episode from Friends and one from Seinfeld as our corpuses (corpi?) as well as an episode from each as our unknown. Each result was the opposite of the real answer (e.g., our model would find that the test episode from Friends was more likely to be from Seinfeld than from Friends.) Prof Dodds told us to test on half an episode instead of a whole one, and this fixed our problem. We then expanded our corpuses to 4 episodes per show and tested on the script from a whole episode instead of a half. We found that our model returned the correct results for the test script from Friends (3-2 in favor of Friends) but still did not return the right result for the Seinfeld test episode.

We did not quite expect these results. Straight up, we thought these would be pretty straightforward wins for one show over the other, especially because of the presence of character names in each show. Still, we think it's possible the models are so close to one another because of the general, everyday language used in sitcoms, and because the scripts contain things like stage cues (Jerry Seinfeld sitting on couch, Kramer walks in) and things like that. """ 

# EXTRA (CREDIT) Text Models: Musicals

print(" +++++++++++ Sondheim Musicals +++++++++++ ")
trained_tm1 = TextModel( "Sondheim" )
text1 = trained_tm1.readTextFromFile( "Sondheim.txt" )
trained_tm1.createAllDictionaries(text1)  # provided in hw description
# trained_tm1.printAllDictionaries()

print(" +++++++++++ Schwartz Musicals +++++++++++ ")
trained_tm2 = TextModel( "Schwartz" )
text2 = trained_tm2.readTextFromFile( "Schwartz.txt" )
trained_tm2.createAllDictionaries(text2)  # provided in hw description
# trained_tm2.printAllDictionaries()

print(" +++++++++++ 1st Test: Wicked +++++++++++ ")
unknown_tm = TextModel( "Test (Wicked)" )
text_unk = unknown_tm.readTextFromFile( "Wicked.txt" )
unknown_tm.createAllDictionaries(text_unk)  # provided in hw description
# unknown_tm.printAllDictionaries()

# print(" +++++++++++ 2nd Test: Into the Woods +++++++++++ ")
# unknown_tm = TextModel( "Test (Into the Woods)" )
# text_unk = unknown_tm.readTextFromFile( "IntotheWoods.txt" )
# unknown_tm.createAllDictionaries(text_unk)  # provided in hw description
# # unknown_tm.printAllDictionaries()

# print(" +++++++++++ 3rd Test: West Side Story +++++++++++ ")
# unknown_tm = TextModel( "Test (West Side Story)" )
# text_unk = unknown_tm.readTextFromFile( "WestSideStory.txt" )
# unknown_tm.createAllDictionaries(text_unk)  # provided in hw description
# # unknown_tm.printAllDictionaries()

unknown_tm.compareTextWithTwoModels(trained_tm1,trained_tm2)

""" For musicals, I created a model of musicals by Stephen Sondheim (Into the Woods and Sweeney Todd), and a model of musicals by Stephen Schwartz (Wicked and Pippin). For my tests, the first 2 returned the correct result, which makes sense because they are excerpts of the musicals scripts in the models. However, for a third test, I wanted to see if a different musical by Sondheim, West Side Story, would return the correct result, and it didn't work. I think for musicals, there is a lot of variability in storyline and song meter, so something like sentence lengths, words, and punctuation can't capture who wrote it. """