import sqlite3
from queries import CREATE_TABLES, SAMPLE_DATA

def init_db():
    # Подключаемся к базе данных (файл создастся автоматически)
    conn = sqlite3.connect('db/shop_db.sqlite')
    cursor = conn.cursor()
    
    # Создаём таблицы
    for table, query in CREATE_TABLES.items():
        cursor.execute(query)
        print(f'Таблица {table} создана')
    
    # Добавляем тестовые данные
    cursor.executemany(
        "INSERT INTO customers VALUES (NULL, ?, ?, ?, ?, ?)",
        SAMPLE_DATA['customers']
    )
    
    cursor.executemany(
        "INSERT INTO orders VALUES (NULL, ?, ?, ?, ?)",
        SAMPLE_DATA['orders']
    )

    cursor.executemany(
        "INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?)",
        SAMPLE_DATA['products']
    )
    
    conn.commit()
    conn.close()
    print("База данных готова!")

if __name__ == "__main__":
    init_db()