import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    print("connected successfully and created the sqlite database")

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()
    print("Insert the value to the",item , " database ")

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()
    print("Deleted the item :", item, " from  database ")

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()
    print("updated the item :", item, " in database with new value" , "\n","item: ", item ,"\n","quantity: " , quantity , "\n" ,"price:", price )
#delete("Coffee Cup")
#insert("Coffee Cup",10,5)
#update(15,7,"Coffee Cup")

print(view())