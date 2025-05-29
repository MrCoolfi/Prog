import sqlite3
from pypika import Query, Table

def main():
    # Подключение к базе данных
    conn = sqlite3.connect('wildberries.db')
    cur = conn.cursor()

    products = Table('wb_products')
    ratings = Table('wb_ratings')
    
    q = Query.from_(products) \
        .join(ratings) \
        .on(products.id == ratings.product_id) \
        .select(products.title, products.price, ratings.rating)
    
    sql = q.get_sql()
    cur.execute(sql)
    rows = cur.fetchall()
    
    # Вывод результатов
    print("Список товаров с ценами и рейтингами:")
    for title, price, rating in rows:
        print(f"{title} - {price}₽ (рейтинг: {rating}/5)")
    
    conn.close()

if __name__ == "__main__":
    main()