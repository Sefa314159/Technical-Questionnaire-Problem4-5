import sqlite3

con = sqlite3.connect("lib.db")

cursor1 = con.cursor()

cursor2 = con.cursor()

def create_table():
    
    cursor1.execute("CREATE TABLE IF NOT EXISTS i_users (userld INT, username TEXT, emailaddress TEXT, isActive BOOLEAN, password TEXT, gender TEXT)") 
    
    cursor2.execute("CREATE TABLE IF NOT EXISTS i_user_login_logs (userld INT, login_date TEXT)")
    
    con.commit() 

        
def more_than_three():
    
    lst = []
    
    cursor1.execute("Select userld, username, emailaddress From i_users") 
    
    cursor2.execute("Select userld From i_user_login_logs")
    
    data1 = cursor1.fetchall()
    
    data2 = cursor2.fetchall()
    
    for i in range(0, len(data2)):
        lst.append(data2[i])
        
    lst2 = []
    
    for i in range(1, 12):
        if(lst.count((i,)) > 3):
            lst2.append(i)
    if(1 in lst2):
        lst2.pop(0)
        
    for user in data1:
        if user[0] in lst2:
            print(user)
more_than_three()

con.close()
