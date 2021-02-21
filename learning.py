from __future__ import unicode_literals
import json
from hazm import *
import sqlite3
from utils import Util

class Learner:
    def learningIntent(self):
        print("learning intents")
        conn = sqlite3.connect("ai_db.db")
        cur = conn.cursor()
        j = open('weights.json' , 'r')
        weights = json.load(j)
        j.close()
        l = cur.execute("select text , label from sample")
        #stopwords = list(open('resources/stopwords.txt' , 'r' , encoding="utf8").read().splitlines())
        weights , lx  = self.weightsCalculator(weights , list(l) , 16)
        j = open("weights.json" , "w")
        json.dump(weights,j)
        j.close()
        cur.close()
        conn.close()
        print(lx , sum(lx))
        return(lx , sum(lx))


    def learningArgument(self):
        print("learning arguments")
        conn = sqlite3.connect("ai_db.db")
        cur = conn.cursor()
        j = open('argWeights.json' , 'r')
        j2 = open('phaseTags.json' , 'r')
        weights = json.load(j)
        tags = json.load(j2)
        j.close()
        j2.close()
        l = cur.execute("select text , label from testSet")
        normalizer = Normalizer()
        final_list = []
        u = Util()
        #lx = u.makeZeroList(16)
        s_i = -1
        for sample in list(l)[:115]:
            s_i += 1
            text = sample[0]
            intent = sample[1]
            print(s_i + 1)
            
            s = u.text_proccessor(text)
            print(s)
            #activation_list = u.makeZeroList(numberOfClasses)
            w_i = -1
            len_s = len(s)
            for word in s:
                w_i += 1
                if not word in weights.keys():
                    # 1 for sum of word and 7 for number of tags => 1 + 7 == 8
                    weights[word] = {}
                    weights[word] = u.makeZeroList(8)

                tag = tags[s_i][w_i]
                weights[word][tag] += 1
                weights[word][-1] += 1

        j = open("argWeights.json" , "w")
        json.dump(weights,j)
        j.close()
        cur.close()
        conn.close()  

    def weightsCalculator(self , weights , samples , numberOfClasses):

        u = Util()
        lx = u.makeZeroList(numberOfClasses)
        for sample in samples:
            real_label = int(sample[1])
            text = sample[0]
            
            s = u.text_proccessor(text)
            activation_list = u.makeZeroList(numberOfClasses)
            for i in s:
                if not i in weights.keys():
                    weights[i] = u.makeZeroList(numberOfClasses)

                for a in range(numberOfClasses):
                    activation_list[a] += weights[i][a]

            # update weights
            estimate_label = u.argMax(activation_list)
            #print(estimate_label , real_label)
            if estimate_label != real_label:
                lx[real_label] += 1
                for i in s:
                    for a in range(numberOfClasses):
                        if a == real_label:
                            weights[i][a] += 1
                        else:
                            weights[i][a] -= 1
        return weights , lx


if __name__ == "__main__":
    l = Learner()
    lx = l.learningIntent()
    while sum(lx[0]) > 0:
        lx = l.learningIntent()
    l.learningArgument()

