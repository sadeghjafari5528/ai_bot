import json

class initializer:

    def initialize(self):
        j = open('weights.txt' , 'w')
        data = {}
        json.dump(data,j)
        j.close()

if __name__ == "__main__":
    init = initializer()
    init.initialize()