from __future__ import unicode_literals
import json
from hazm import *
import sqlite3
from utils import Util

class Tester:

    def testing(self):
        print("testing")
        u = Util()
        conn = sqlite3.connect("ai_db.db")
        cur = conn.cursor()
        l = cur.execute("select text , label from testSet")
        j = open('weights.json' , 'r')
        weights = json.load(j)
        j.close()
        no_test = 0
        no_currect = 0
        #stopwords = list(open('resources/stopwords.txt' , 'r' , encoding="utf8").read().splitlines())
        lx = u.makeZeroList(16)
        
        for test in list(l):
            real_label = int(test[1])
            text = test[0]
            
            s = u.text_proccessor(text)
            #s = l.deleteStopWords(s , stopwords)
            activation_list = u.makeZeroList(16)
            for i in s:
                if not i in weights.keys():
                    weights[i] = u.makeZeroList(16)

                for a in range(16):
                    activation_list[a] += weights[i][a]

            # calculate result
            estimate_label = u.argMax(activation_list)
            #print(estimate_label)
            no_test += 1
            if estimate_label == real_label:
                no_currect += 1
            else:
                lx[real_label] += 1
                print(real_label , estimate_label)
        print("result : " , int(no_currect/no_test * 100))
        print(lx , sum(lx))
        cur.close()
        conn.close()
if __name__ == "__main__":
    t = Tester()
    t.testing()