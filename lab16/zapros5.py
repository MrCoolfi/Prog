import sqlite3
from pypika import Query, Table, functions as fn

conn = sqlite3.connect('wildberries.db')
cur = conn.cursor()

products = Table('wb_products')
reviews = Table('wb_ratings')

q = Query.from_(products) \
    .join(reviews) \
    .on(products.id == reviews.product_id) \
    .select(fn.Max(products.price).as_("max_price")) \
    .where(reviews.rating >= 3)

sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for row in rows:
    print(f"Максимальная цена товаров с рейтингом 3+: {row[0]} руб")

conn.close()