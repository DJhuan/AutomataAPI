import sqlite3
import pickle

def setup():
    con = sqlite3.connect('atoapi.db')
    con.cursor().execute('''CREATE TABLE IF NOT EXISTS automatos (id INTEGER PRIMARY KEY, automato BLOB)''')
    con.commit()

async def insert(automato):
    con = sqlite3.connect('atoapi.db')
    result = con.cursor().execute('''INSERT INTO automatos (automato) VALUES (?) RETURNING id''', (pickle.dumps(automato),))
    result = result.fetchone()
    con.commit()
    return result
    

def find(id):
    con = sqlite3.connect('atoapi.db')
    result = con.cursor().execute('''SELECT automato FROM automatos WHERE id = ?''', (id,)).fetchone()
    if result == None:
        return None
    result = pickle.loads(result[0])
    return result

def delete(id):
    con = sqlite3.connect('atoapi.db')
    maquina = con.cursor().execute('''SELECT id FROM automatos WHERE id = ?''', (id,)).fetchone()
    if maquina == None:
        con.commit
        return "Máquina inexistente."
    else:
        con.cursor().execute('''DELETE FROM automatos WHERE id = ?''', (id,))
        con.commit()
        return "Deleção bem sucedida!"