

file = open("training_set1.txt" , 'r')
result = open('training_set2.txt' , 'w')

while True:
    line = file.readline() 
    if not line: 
        break
    print(line)
    text = line.split("/")
    print(text[0] , text[1])
    text = text[1][:-1] + "/" + text[0]
    #print(text)

    result.writelines(text + "\n")
file.close()
result.close()