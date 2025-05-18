# Все SQL-запросы для базы данных
CREATE_TABLES = {
    'customers': """
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        address TEXT NOT NULL
    )
    """,
    
    'products': """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL DEFAULT 0,
        category TEXT
    )
    """,
    
    'orders': """
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        order_date TEXT DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL DEFAULT 'pending',
        total_amount REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
    """
}

SAMPLE_DATA = {
    'customers': [
        ('Иван', 'Иванов', 'ivan@mail.ru', '+79161112233', 'Москва, ул. Ленина 1'),
        ('Петр', 'Петров', 'petr@mail.ru', '+79162223344', 'Санкт-Петербург, Невский пр. 5')
    ],
    'orders': [
        (24515, '2023-05-15 14:30:00', 'completed', 89999.99),
        (27821, '2023-05-20 10:15:00', 'processing', 59999.99)
    ],
    'products': [
        ('Ноутбук', 'Мощный игровой ноутбук', 89999.99, 10, 'Электроника'),
        ('Смартфон', 'Новый флагман', 59999.99, 15, 'Электроника')
    ]
}