from src.database import Database
from src.parser import parse_wikipedia_buildings
from src.queries import BuildingQueries
import time

def main():
    print("=== Анализ высотных зданий мира ===")
    start_time = time.time()
    
    # Инициализация БД
    db = Database()
    if not db.connect() or not db.create_tables():
        print("Ошибка инициализации БД")
        return
    
    # Парсинг данных
    print("\nЗагрузка данных с Wikipedia...")
    buildings_data = parse_wikipedia_buildings()
    
    if not buildings_data:
        print("Не удалось получить данные")
        db.close()
        return
    
    # Сохранение данных
    print("\nСохранение данных в БД...")
    success_count = 0
    for building in buildings_data:
        if db.insert_building(building):
            success_count += 1
    
    print(f"Успешно сохранено {success_count} зданий")
    
    # Выполнение запросов
    queries = BuildingQueries(db)
    
    print("\nТоп-5 стран по количеству зданий:")
    if top_countries := queries.get_top_countries(5):
        for country, count in top_countries:
            print(f"{country}: {count} зданий")
    
    print("\nСуммарная высота 50 самых высоких зданий:")
    if total_height := queries.get_total_height_top_n(50):
        print(f"{total_height:.2f} километров")
    
    print("\nСамые высокие здания:")
    if tall_buildings := queries.get_tallest_buildings(5):
        for name, country, height, year, b_type in tall_buildings:
            print(f"{name} ({country}, {year}): {height} м, тип: {b_type}")
    
    # Завершение
    db.close()
    print(f"\nПрограмма завершена за {time.time() - start_time:.2f} секунд")

if __name__ == "__main__":
    main()