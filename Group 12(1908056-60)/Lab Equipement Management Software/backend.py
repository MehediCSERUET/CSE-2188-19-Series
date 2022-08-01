import sqlite3

def connection():
  conn=sqlite3.connect('book.db')
  conn.execute('CREATE TABLE if not exists lab (id integer PRIMARY KEY AUTOINCREMENT, equipement_name text not null, company_name text not null, date_of_entry integer, index1 text)')
  conn.commit()
  conn.close()

def insert(equipement_name,company_name,date_of_entry,index1):
  conn=sqlite3.connect('book.db')
  conn.execute("INSERT INTO lab VALUES (NULL,?,?,?,?)",(equipement_name,company_name,date_of_entry,index1))
  conn.commit()
  conn.close()

def view():
  conn=sqlite3.connect('book.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from lab")
  rows=cur_obj.fetchall()
  conn.close()
  return rows

def update(id,equipement_name,company_name,date_of_entry,index1):
  conn=sqlite3.connect('book.db')
  conn.execute("UPDATE lab SET equipement_name=?,company_name=?,date_of_entry=?,index1=? WHERE id=?",(equipement_name,company_name,date_of_entry,index1,id))
  conn.commit()
  conn.close()

def delete(id):
  conn=sqlite3.connect('book.db')
  conn.execute("DELETE from lab WHERE id=?",(id,))
  conn.commit()
  conn.close()

def search(equipement_name='',company_name='',date_of_entry='',index1=''):
  conn=sqlite3.connect('book.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from lab WHERE equipement_name=? OR company_name=? OR date_of_entry=? OR index1=?",(equipement_name,company_name,date_of_entry,index1))
  rows=cur_obj.fetchall()
  conn.close()
  return rows

connection()


def data entry