import math

class TfIdf:
	def __init__(self):
		self.corpus = {}
		self.words = {}
		self.tot_words = {}
		
		self.idf = 0
		self.tf = {}
		self.tf_idf = {}

	def add_corpus(self, name):
		# Lecture du fichier donné
		with open(f"corpus/{name}", "r") as f:
			self.txt = f.read()

		# on sépare chaque mot avec le caractère " "
		split_txt = self.txt.split(" ")
		
		self.corpus[name] = {}
		self.tot_words[name] = 0
		
		# vérification de si un mot est déjà ou pas dans les dictionnaires
		for i in split_txt:
			
			# si oui, ajouter 1 à sa valeur
			if i in self.words.keys():
				self.words[str(i)] += 1
			# sinon on l'initie avec la valeur 1
			else:
				self.words[str(i)] = 1
			
			if i in self.corpus[name].keys():	
				self.corpus[name][str(i)] += 1
			else:
				self.corpus[name][str(i)] = 1
			self.tot_words[name] += 1
	
	def get_idf(self, word):
		self.word = word
		self.count = 0
		for i in self.corpus:
			if word in self.corpus[i].keys():
				self.count += 1
		return math.log(len(self.corpus) / self.count)

	def get_tf_idf(self, corpus_name):
		for word in self.corpus[corpus_name].keys():
			self.tf[word] = self.corpus[corpus_name][word] / self.tot_words[corpus_name]
			self.tf_idf[word] = self.tf[word] * self.get_idf(word)
			for i in self.words.keys():
				if not i in self.corpus[corpus_name].keys():
					self.tf_idf[i] = 0
		return self.tf_idf

	def cos_sim(self, corpus1, corpus2):
		tf_idf_a = self.get_tf_idf(corpus1)
		tf_idf_b = self.get_tf_idf(corpus2)
		self.ab = 0
		for word in self.words.keys():
			self.ab += (tf_idf_a[word] * tf_idf_b[word])
		self.a = 0
		self.b = 0
		for word in self.words.keys():
			self.a += tf_idf_a[word] ** 2
			self.b += tf_idf_b[word] ** 2
		self.a = math.sqrt(self.a)
		self.b = math.sqrt(self.b)
		return self.ab / (self.a * self.b)
