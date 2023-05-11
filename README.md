## Fast Portuguese Lemmatizer
Extract lemma* from portuguese words.

> This repo aims to store code for a Portuguese Lemmatizer - inpired by @JeffersonLPLima

*_A lemma is a word that stands at the head of a definition in a dictionary._ [Wikipedia](https://simple.wikipedia.org/wiki/Lemma_(linguistics)#:~:text=A%20lemma%20is%20a%20word,you%20find%20in%20the%20dictionary.)
### Example
```
from pt_lemma import Lemmatizer

l = Lemmatizer()
l.get_lemma('carrinho')  #all words must be unidecoded and lowercased
>> 'carro'
l.get_lemma('carros')
>> 'carro'

```
### Files:

`pt_lemma.py` :  Simple class to perform lemmatization

`./data/`:  data used to generate lemma dict