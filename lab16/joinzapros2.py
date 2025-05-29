import sqlite3
from pypika import Query, Table, functions as fn

def main():
    conn = sqlite3.connect('wildberries.db')
    cur = conn.cursor()
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='wb_products'")
    if not cur.fetchone():
        print("Ошибка: таблица wb_products не найдена")
        conn.close()
        return
    
    products = Table('wb_products')
    ratings = Table('wb_ratings')

    q = Query.from_(products) \
        .join(ratings) \
        .on(products.id == ratings.product_id) \
        .select(products.title, products.price, ratings.rating) \
        .where(ratings.rating == 5)
    
    sql = q.get_sql()
    cur.execute(sql)
    rows = cur.fetchall()
    
    if rows:
        print("\nТовары с рейтингом 5:")
        for i, (title, price, rating) in enumerate(rows, 1):
            print(f"{i}. {title} - {price}₽ (рейтинг: {rating}/5)")
    else:
        print("\nТовары с рейтингом 5 не найдены")
    
    conn.close()

if __name__ == "__main__":
    main()