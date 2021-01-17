import json

def initialize():
    j = open('weights.txt' , 'w')
    data = {}
    json.dump(data,j)
    j.close()

initialize()