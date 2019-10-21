import sqlite3
def userRegistration(uname,passwd):
    conn = sqlite3.connect("note.db")
    conn.execute("INSERT INTO users(username,password) VALUES(?,?)",(uname,passwd,))
    conn.commit()
    conn.close()

def userLogin(uname,passwd):
    conn = sqlite3.connect("note.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?",(uname,))
    rows = cur.fetchone()
    ret = 0
    try:
        if rows[1] == uname and rows[2] == passwd:
            print("doru")
            ret = rows[0]
        else:
            ret = 0
    except:
        ret = 0
    conn.close()
    return ret

def noteAdd(uid,head,txt):
    conn = sqlite3.connect("note.db")
    conn.execute("INSERT INTO notes(noteHeader,noteText,userId) VALUES(?,?,?)", (head,txt,uid))
    conn.close()

def noteRemove(uid,noteNumber):
    conn = sqlite3.connect("note.db")
    cur = conn.cursor()
    cur.execute("SELECT userId FROM notes WHERE noteNumber=?", (noteNumber,))
    rows = cur.fetchone()
    ret = ""
    if rows[0] == uid:
        conn.execute("DELETE FROM notes WHERE noteNumber=?", (noteNumber,))
        ret = "Operation completed"
    else:
        ret = "Unauthorized operation"
    conn.close()
    return ret

