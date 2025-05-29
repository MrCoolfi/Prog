import sqlite3
from pypika import Query, Table, functions as fn

conn = sqlite3.connect('wildberries.db')
cur = conn.cursor()

products = Table('wb_products')
reviews = Table('wb_ratings')

q = Query.from_(reviews) \
    .select(reviews.rating, fn.Count(reviews.id).as_("count")) \
    .groupby(reviews.rating)

sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

print("Статистика по рейтингам товаров:")
for rating, count in rows:
    print(f"Рейтинг {rating}: {count} товаров")

conn.close()