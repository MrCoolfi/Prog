import sqlite3
from db.queries import CREATE_TABLES

class OnlineShop:
    def __init__(self):
        self.conn = sqlite3.connect('db/shop_db.sqlite')
        self.cursor = self.conn.cursor()
    
    def show_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        for product in self.cursor.fetchall():
            print(product)
    
    def show_all_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        for customer in self.cursor.fetchall():
            print(customer)

    def show_all_orders(self):
        self.cursor.execute("SELECT * FROM orders")
        for orders in self.cursor.fetchall():
            print(orders)
    
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    shop = OnlineShop()
    
    print("\nВсе товары:")
    shop.show_all_products()
    
    print("\nВсе покупатели:")
    shop.show_all_customers()

    print("\nВсе заказы:")
    shop.show_all_orders()
    
    shop.close()    