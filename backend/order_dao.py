from datetime import  datetime
from db_connection import db_connect
def get_all_orders(connction):
    cursor = connction.cursor()

    query = "SELECT * FROM grocery_store.orders;"
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total_price, time) in cursor:
        response.append({
            'order_id':order_id,
            'customer_name': customer_name,
            'total': total_price,
            'datetime': time
        })
    print(response)
    return(response)

def insert_order(connection, order):
    cursor = connection.cursor()
    query = ("insert into orders"
            "(customer_name, total_price, time)"
            " VALUES (%s, %s, %s);")
    data = (order['customer_name'], order['total'], datetime.now())
    cursor.execute(query, data)
    connection.commit()
    order_id = cursor.lastrowid
    order_details_query = ("insert into order_details"
                           "(order_id, product_id, total_price, quantity)"
                           "values (%s, %s, %s, %s);"
                           )

    order_details_data = []
    for order_detail in order['order_details']:
        order_details_data.append([
            order_id, int(order_detail['product_id']),
            float(order_detail['total_price']),
            float(order_detail['quantity'])
        ])
    cursor.executemany(order_details_query, order_details_data)
    connection.commit()
    #print("inserted successfully")


    # connection.close()
    return order_id


if __name__ == "__main__":
    connection = db_connect()
    order = {
        'customer_name': 'beso',
        'total':300,
        'order_details': [{
            'product_id': 3,
            'quantity': 2,
            'total_price': 20
        },
        {
            'product_id': 3,
            'quantity': 3,
            'total_price': 50
        }]
    }
    print(insert_order(connection, order))


