import pytest
import os
from src.database import Database
from src.config import DATABASE

@pytest.fixture
def test_db():
    # Удаляем тестовую базу, если она существует
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    
    db = Database()
    db.connect()
    db.create_tables()
    yield db
    db.close()
    if os.path.exists(DATABASE):
        os.remove(DATABASE)

def test_database_connection(test_db):
    """Проверяем подключение к базе данных"""
    assert test_db.conn is not None

def test_tables_creation(test_db):
    """Проверяем создание таблиц"""
    cursor = test_db.conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    assert 'Countries' in tables
    assert 'BuildingTypes' in tables
    assert 'Buildings' in tables

def test_insert_building(test_db):
    """Проверяем добавление здания"""
    test_data = {
        'name': 'Test Building',
        'city': 'Test City',
        'country': 'Test Country',
        'height': 100.0,
        'year': 2023,
        'type': 'Test Type'
    }
    
    assert test_db.insert_building(test_data)
    
    # Проверяем, что данные добавились
    cursor = test_db.conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Buildings")
    assert cursor.fetchone()[0] == 1