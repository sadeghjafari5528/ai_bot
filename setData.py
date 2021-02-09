import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("ai_db.db")
    cur = conn.cursor()

    file = open("training_set2.txt" , 'r')
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
            cur.execute("INSERT INTO sample (" + column + ") VALUES(" + values + ");")
        except:
            continue
        #l = cur.execute("SELECT sql FROM sqlite_master WHERE tbl_name = 'sample' AND type = 'table'")
    conn.commit()
    cur.close()
    conn.close()
    file.close()