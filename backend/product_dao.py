from db_connection import db_connect

def get_all_the_products(connection):

    cursor = connection.cursor()

    query = "SELECT * FROM sample.products;"
    query2 =("SELECT products.product_id, products.fName, products.uom_id, uom.uom_name, products.price_per_unit "
            "FROM products inner join uom on products.uom_id = uom.uom_id;")

    cursor.execute(query2)
    response = []
    for (product_id, fName, uom_id, uom_name, price_per_unit) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'fName': fName,
                'uom_id': uom_id,
                'uom_name': uom_name,
                'price_per_unit': price_per_unit
            }
        )
        #print(product_id, fName, uom_id, uom_name, price_per_unit)

    #connection.close()
    return response

def insert_new_product(connection, product):
        cursor = connection.cursor()
        query = ("insert into products "
                 "(fName, uom_id, price_per_unit) "
                 " values (%s, %s, %s);")
        data = (product['product_name'], product['uom_id'], product['price_per_unit'])
        cursor.execute(query, data)
        connection.commit()
        print("inserted successfully")
        temp = cursor.lastrowid
        #connection.close()
        return temp

def delete_product(connection, product_id):
        cursor = connection.cursor()
        query = "delete from products where product_id = (%s);"

        data = (str(product_id), )
        cursor.execute(query, data)

        connection.commit()
        print("deleted successfully")
        return product_id

def try_some_select(connection, id):
        cursor = connection.cursor()

        query = "select * from products where product_id =" + str(id) + ";"
        cursor.execute(query)

        print("found" if len(cursor.fetchone()) else "not found")
if __name__ == "__main__":
    connection = db_connect()
    '''insert_new_product(connection, {
            'name': 'orange',
            'uom':'1',
            'price':'30'
    })'''
    #print(get_all_the_products(connection))
    #delete_product(connection, 12)
    try_some_select(connection, 1)

