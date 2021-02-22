import json

class initializer:

    def initializeIntent(self):
        j = open('weights.json' , 'w')
        data = {}
        json.dump(data,j)
        j.close()

    def initializeArgumnet(self):
        j = open('argWeights.json' , 'w')
        data = {}
        json.dump(data,j)
        j.close()        

if __name__ == "__main__":
    init = initializer()
    command = input("enter your initializer type : (intent , argument)")
    if command == 'intent':
        init.initializeIntent()
    elif command == 'argument':
        init.initializeArgumnet()
    