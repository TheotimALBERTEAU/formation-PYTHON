from Classes.TfIdf import TfIdf

# premiers tests
t = TfIdf()
t.add_corpus("test")
t.add_corpus("toast")

"""
print(t.words)
print("----------------------------------------------")
print(t.corpus)
print(t.tot_words)
"""

# crée instance de TfIdf
TfIdf = TfIdf()

# Ajouter tous les corpus
TfIdf.add_corpus("corpus_7z")
TfIdf.add_corpus("corpus_Deafness")
TfIdf.add_corpus("corpus_Disability")
TfIdf.add_corpus("corpus_EPUB")
TfIdf.add_corpus("corpus_France")
TfIdf.add_corpus("corpus_Germany")
TfIdf.add_corpus("corpus_Island")
TfIdf.add_corpus("corpus_Karate")
TfIdf.add_corpus("corpus_MMA")
TfIdf.add_corpus("corpus_Ninja")
TfIdf.add_corpus("corpus_PDF")
TfIdf.add_corpus("corpus_Sign_language")

# test des méthodes
# TfIdf.get_idf("karate")
# TfIdf.get_tf_idf("corpus_Ninja")
# print(TfIdf.cos_sim("corpus_Deafness", "corpus_MMA"))
