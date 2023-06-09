import unidecode
import pickle
import os

class Lemmatizer():
    def __init__(self):
        if (os.path.exists('pt_lemmatizer/lemmatizer.pickle')):
            print('loading lemmatizer dict (pt_lemmatizer/lemmatizer.pickle)')
            self.lemmatizer_dict = self.load_lemmatizer_dict()
        else:
            print('generating lemmatizer dict (pt_lemmatizer/lemmatizer.pickle)')
            self.lemmatizer_dict = self.generate_lemmatizer_dict()

    def generate_lemmatizer_dict(self):
        file_name = 'pt_lemmatizer/data/lemmatization-pt.txt'

        with open(file_name, encoding="utf-8") as f:
            lemmatizer_dict = {}
            for l in list(f)[1:]:
                words = l.rstrip().split("\t")
                word = unidecode.unidecode(words[0]).strip().lower()
                infl = unidecode.unidecode(words[1]).strip().lower()
                if (len(set(word)) > 1):
                    if (word not in lemmatizer_dict.keys()):
                        lemmatizer_dict[word] = [infl]
                    else:
                        lemmatizer_dict[word].append(infl)
        inverse_lemmatizer_dict = {}
        for k, v in lemmatizer_dict.items():
            for w in v:
                inverse_lemmatizer_dict[w] = k

        pickle.dump(inverse_lemmatizer_dict, open("pt_lemmatizer/lemmatizer.pickle", "wb"))
        return inverse_lemmatizer_dict

    def load_lemmatizer_dict(self):
        return pickle.load(open("pt_lemmatizer/lemmatizer.pickle", "rb"))

    def lemmatize(self, word):
        return self.lemmatizer_dict.get(word, word)

if __name__ == '__main__':
    l = Lemmatizer()
    w = 'apagou'
    print("word:", w)
    print("lemma:", l.lemmatize(w))