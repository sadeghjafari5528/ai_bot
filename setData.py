import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("ai_db.db")
    cur = conn.cursor()

    file = open("test_set.txt" , 'r')
    column = "text," + "time," + "weather," + "occasion," + "rt"
    values = ""
    switch = {1:"0,1,0,0",
              2:"0,0,0,1",
              3:"1,0,0,0",
              4:"0,0,1,0",
              0:"0,0,0,0"}
    while True:
        line = file.readline() 
        if not line: 
            break
        text = line.split("/")
        values = "'" + text[0] + "'," + switch[int(text[1])]
        
        try:
            cur.execute("INSERT INTO testSet (" + column + ") VALUES(" + values + ");")
        except:
            continue
        #l = cur.execute("SELECT sql FROM sqlite_master WHERE tbl_name = 'sample' AND type = 'table'")
    conn.commit()
    cur.close()
    conn.close()

'''result = open('training_set2.txt' , 'w')

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
result.close()'''
