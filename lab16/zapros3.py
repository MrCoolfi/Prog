import sqlite3
from pypika import Query, Table, functions as fn

conn = sqlite3.connect('wildberries.db')
cur = conn.cursor()

products = Table('wb_products')

q = Query.from_(products).select(fn.Avg(products.price).as_("avg_price"))

sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for avg_price in rows:
    print(f"Средняя цена товаров: {avg_price[0]:.2f}₽")

conn.close()