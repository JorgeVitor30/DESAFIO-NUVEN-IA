import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


def tokenize(sentence):
    """
    **Tokenização**
    Dividir a frase em um array de palavras/ tokens. Um token pode ser uma palavra, um caractere de pontuação ou um número.
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    Stemming = encontrar a forma base da palavra
    Exemplo: pegar verbos no passado e presente e transformá-los em sua forma base.
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """"
    Cria um vetor de palavras para representar a similaridade dos tokens com as palavras.
    """
    sentence_words = [stem(word) for word in tokenized_sentence]

    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag