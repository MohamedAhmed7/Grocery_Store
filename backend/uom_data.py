def get_uom(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM grocery_store.uom;"
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        print(uom_id , uom_name)
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response
if __name__ == "__main__":
    from db_connection import db_connect
    connection = db_connect()
    print(get_uom(connection))