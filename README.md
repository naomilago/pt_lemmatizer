## Fast Portuguese Lemmatizer
Extract *lemma* from portuguese words.

> This repo aims to store code for a Portuguese Lemmatizer PyPI library - a python package inpired by @JeffersonLPLima code.

*_A lemma is a word that stands at the head of a definition in a dictionary._* [Wikipedia](https://simple.wikipedia.org/wiki/Lemma_(linguistics)#:~:text=A%20lemma%20is%20a%20word,you%20find%20in%20the%20dictionary.)
### Example
```
from pt_lemmatizer import Lemmatizer

l = Lemmatizer()
l.lemmatize('apagou')  #all words must be unidecoded and lowercased
>> 'apagar'
l.lemmatize('nasalaram')
>> 'nasalar'

```
### Files:

`pt_lemma.py` :  Simple class to perform lemmatization

`./data/`:  data used to generate lemma dict