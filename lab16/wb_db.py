import sqlite3
from wb_parser import get_wildberries_items

def main():
    print("Начало парсинга Wildberries...")
    items = get_wildberries_items()
    
    if not items:
        print("Не удалось найти товары. Возможные причины:")
        print("- Изменилась структура сайта")
        print("- Проблемы с подключением")
        print("- Требуется ручное обновление селекторов")
        return
    
    print(f"\nУспешно найдено товаров: {len(items)}")
    print("Примеры найденных товаров:")
    for i, item in enumerate(items[:3], 1):
        print(f"{i}. {item['title']} - {item['price']}₽")

    # Создание БД с правильными названиями таблиц
    conn = sqlite3.connect("wildberries.db")
    c = conn.cursor()
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS wb_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL
        )
    """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS wb_ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            rating INTEGER,
            FOREIGN KEY(product_id) REFERENCES wb_products(id)
        )
    """)
    
    # Вставка данных
    for item in items:
        c.execute("INSERT INTO wb_products (title, price) VALUES (?, ?)", 
                 (item["title"], item["price"]))
        c.execute("INSERT INTO wb_ratings (product_id, rating) VALUES (?, ?)", 
                 (c.lastrowid, item["rating"]))
    
    conn.commit()
    conn.close()
    print("\nДанные сохранены в wildberries.db")

if __name__ == "__main__":
    main()