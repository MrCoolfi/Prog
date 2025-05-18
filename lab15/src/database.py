import sqlite3
from sqlite3 import Error
from typing import List, Dict, Optional
from .config import DATABASE
import os

class Database:
    def __init__(self):
        self.conn = None
        
    def connect(self) -> bool:
        try:
            os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
            self.conn = sqlite3.connect(DATABASE)
            self.conn.execute("PRAGMA foreign_keys = ON")
            return True
        except Error as e:
            print(f"Ошибка подключения: {str(e)}")
            return False
    
    def create_tables(self) -> bool:
        sql_scripts = [
            """CREATE TABLE IF NOT EXISTS Countries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS BuildingTypes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_name TEXT UNIQUE NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS Buildings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                city TEXT NOT NULL,
                country_id INTEGER NOT NULL,
                height REAL NOT NULL,
                year INTEGER NOT NULL,
                type_id INTEGER NOT NULL,
                FOREIGN KEY (country_id) REFERENCES Countries(id),
                FOREIGN KEY (type_id) REFERENCES BuildingTypes(id))"""
        ]
        
        try:
            cursor = self.conn.cursor()
            for script in sql_scripts:
                cursor.execute(script)
            self.conn.commit()
            return True
        except Error as e:
            print(f"Ошибка создания таблиц: {str(e)}")
            return False
    
    def insert_building(self, building_data: Dict) -> bool:
        try:
            cursor = self.conn.cursor()
            
            # Добавляем страну
            cursor.execute(
                "INSERT OR IGNORE INTO Countries (name) VALUES (?)",
                (building_data['country'],)
            )
            
            # Добавляем тип
            cursor.execute(
                "INSERT OR IGNORE INTO BuildingTypes (type_name) VALUES (?)",
                (building_data['type'],)
            )
            
            # Получаем ID страны и типа
            cursor.execute(
                "SELECT id FROM Countries WHERE name = ?",
                (building_data['country'],)
            )
            country_id = cursor.fetchone()[0]
            
            cursor.execute(
                "SELECT id FROM BuildingTypes WHERE type_name = ?",
                (building_data['type'],)
            )
            type_id = cursor.fetchone()[0]
            
            # Добавляем здание (OR REPLACE для обновления дубликатов)
            cursor.execute(
                """INSERT OR REPLACE INTO Buildings 
                (name, city, country_id, height, year, type_id)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    building_data['name'],
                    building_data['city'],
                    country_id,
                    building_data['height'],
                    building_data['year'],
                    type_id
                )
            )
            
            self.conn.commit()
            return True
        except Error as e:
            print(f"Ошибка добавления здания: {str(e)}")
            return False
    
    def execute_query(self, query: str, params: tuple = ()) -> Optional[List[tuple]]:
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Ошибка выполнения запроса: {str(e)}")
            return None
    
    def close(self):
        if self.conn:
            self.conn.close()