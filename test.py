from __future__ import unicode_literals
import json
from hazm import *
from learning import learner

class tester:

    def testing(self):
        print("testing")
        l = learner()
        file = open("test_set.txt" , 'r')
        j = open('weights.txt' , 'r')
        weights = json.load(j)
        j.close()
        no_test = 0
        no_currect = 0
        lx = [0,0,0,0,0]
        #stopwords = list(open('resources/stopwords.txt' , 'r' , encoding="utf8").read().splitlines())
        while True:
            # Get next line from file 
            line = file.readline() 
            # if line is empty 
            # end of file is reached 
            if not line: 
                break

            text = line.split("/")
            real_label = int(text[1])
            text = text[0]
            
            s = l.text_proccessor(text)
            #s = l.deleteStopWords(s , stopwords)
            activation_list = [0,0,0,0,0]
            for i in s:
                if not i in weights.keys():
                    weights[i] = [0,0,0,0,0]

                for a in range(5):
                    activation_list[a] += weights[i][a]

            # calculate result
            estimate_label = l.argMax(activation_list)
            #print(estimate_label)
            no_test += 1
            if estimate_label == real_label:
                no_currect += 1
            else:
                lx[real_label] += 1
        print("result : " , int(no_currect/no_test * 100))
        print(lx , sum(lx))
        file.close()
if __name__ == "__main__":
    t = tester()
    t.testing()