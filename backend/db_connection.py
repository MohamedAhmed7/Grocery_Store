import mysql.connector
__cnx = None
def db_connect():
    db = 'grocery_store'
    pwd = '@#$mohamed01122230207'
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password=pwd,
                                      host='127.0.0.1',
                                      database=db)
        print("connected successfully to " + db + " db")
    return __cnx