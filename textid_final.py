#JennyY(Yuqing) Cang, Grace Stewart, and Umar Farooq
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

print(" +++++++++++ Model1 +++++++++++ ")
trained_tm1 = TextModel( "Model1" )
text1 = trained_tm1.readTextFromFile( "train1.txt" )
trained_tm1.createAllDictionaries(text1)  # provided in hw description
trained_tm1.printAllDictionaries()

print(" +++++++++++ Model2 +++++++++++ ")
trained_tm2 = TextModel( "Model2" )
text2 = trained_tm2.readTextFromFile( "train2.txt" )
trained_tm2.createAllDictionaries(text2)  # provided in hw description
trained_tm2.printAllDictionaries()

print(" +++++++++++ Unknown text +++++++++++ ")
unknown_tm = TextModel( "Unknown (trial)" )
text_unk = unknown_tm.readTextFromFile( "unknown.txt" )
unknown_tm.createAllDictionaries(text_unk)  # provided in hw description
unknown_tm.printAllDictionaries()


	# def compareTextWithTwoModels(self,model1,model2):
	# 	""" runs the compareDictionaries method for all feature dictionaries in self against corresponding normalized dictionaries in model1 and model2
	# 	"""
	