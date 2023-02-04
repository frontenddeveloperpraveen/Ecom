import mysql.connector
def connection():

    conn = mysql.connector.connect(host="localhost",user="root",password="root",port="3306",database="django_joes")
    if conn.is_connected:
        cursor1 = conn.cursor()
        q = "select order_id from shop_orderupdate;"
        L = []
        cursor1.execute(q)
        for i in cursor1:
            for j in i:
                L = L + [j]
        id = L[-1]
        q1 = "select email from shop_orders where order_id={};".format(id)
        cursor1.execute(q1)

        for i in cursor1:
            for j in i:
                email = j
        print(id)
        return (id,email)

