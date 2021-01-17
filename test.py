from __future__ import unicode_literals
import json
from hazm import *
from learning import learner

class tester:

    def testing(self):
        l = learner()
        file = open("test_set.txt" , 'r')
        j = open('weights.txt' , 'r')
        weights = json.load(j)
        j.close()
        no_test = 0
        no_currect = 0
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
            activation_list = [0,0,0,0,0]
            for i in s:
                if not i in weights.keys():
                    weights[i] = [0,0,0,0,0]

                for a in range(5):
                    activation_list[a] += weights[i][a]

            # calculate result
            estimate_label = l.argMax(activation_list)
            print(estimate_label)
            no_test += 1
            if estimate_label == real_label:
                no_currect += 1
        print("result : " , int(no_currect/no_test * 100))
        file.close()
if __name__ == "__main__":
    t = tester()
    t.testing()