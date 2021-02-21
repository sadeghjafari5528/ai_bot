from hazm import *
import datetime
from final_code_aibot_first_part.config import *
import functions
from phase_parser.time import timeParser
from phase_parser.date import dateParser

class Util:
    def numberize(self , text_tokenize):
        text_tokenize = functions.sign(text_tokenize)
        text_tokenize = functions.adad_adadi(text_tokenize)
        text_tokenize = functions.adad_farsi(text_tokenize)
        return text_tokenize

    def text_proccessor(self,text):
        normalizer = Normalizer()
        stemmer = Stemmer()
        lemmatizer = Lemmatizer()
        s = word_tokenize(normalizer.normalize(text))
        for i in range(len(s)):
            s[i] = lemmatizer.lemmatize(s[i])

        return s

    def argMax(self,l):
        result = None
        x = "inf"
        for i in range(len(l)):
            if x == "inf":
                x = l[i]
                result = i
            elif l[i] > x:
                x = l[i]
                result = i
        return result

    def deleteStopWords(self , text , stopwords):
        t1 = []
        for w in text:
            if not w[0] in stopwords:
                t1.append(w)
        return t1

    def makeZeroList(self , n):
        l = []
        for i in range(n):
            l.append(0)
        return l

    def makeZeroMatrix(self , i , j):
        result = []
        for n in range(i):
            result.append(self.makeZeroList(j))
        return result


class Parser():
    def cityParser(self , text):
        return text

    def dateParser(self , text):
        return dateParser(text) 

    def timeParser(self , text):
        return text#timeParser(text)

    def religiousTimeParser(self , text):
        return text

    def calendarTypeParser(self , text):
        return text

    def eventParser(self , text):
        return text
