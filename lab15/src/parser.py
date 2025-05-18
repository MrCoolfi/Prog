import requests
from bs4 import BeautifulSoup
import re
from typing import List, Dict
from .config import WIKI_URL

# Словари для ручной коррекции данных
BUILDING_CORRECTIONS = {
    "Merdeka 118": {"height": 678.9, "year": 2022},
    "Тайбэй 101": {"height": 509.2, "year": 2004},
    "Бурдж-Халифа": {"height": 828.0, "year": 2010},
    "Шанхайская башня": {"height": 632.0, "year": 2015}
}

COUNTRY_CORRECTIONS = {
    "Куала-Лунпур": "Куала-Лумпур",
    "Тайбай": "Тайбэй",
    "Панхай": "Шанхай",
    "Гуанчкоу": "Гуанчжоу"
}

def parse_wikipedia_buildings() -> List[Dict]:
    """Усовершенствованный парсер с ручной коррекцией данных"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(WIKI_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})
        
        if not table:
            raise ValueError("Таблица с данными не найдена")
        
        buildings = []
        processed_names = set()
        rows = table.find_all('tr')[1:]
        
        for row in rows:
            try:
                cols = row.find_all('td')
                if len(cols) < 6:
                    continue
                
                # Обработка названия
                name = cols[1].get_text(strip=True).replace('\xa0', ' ')
                if name in processed_names:
                    continue
                processed_names.add(name)
                
                # Обработка города и страны
                city = cols[2].get_text(strip=True)
                country = cols[3].get_text(strip=True)
                country = COUNTRY_CORRECTIONS.get(country, country)
                
                # Обработка высоты
                if name in BUILDING_CORRECTIONS:
                    height = BUILDING_CORRECTIONS[name]["height"]
                else:
                    height_text = cols[4].get_text(strip=True)
                    height_match = re.search(r'(\d+[\.,]?\d*)', height_text)
                    height = float(height_match.group(1).replace(',', '.')) if height_match else 0.0
                    if height > 1000:  # Автокоррекция явных ошибок
                        height = height / 10
                
                # Обработка года
                if name in BUILDING_CORRECTIONS:
                    year = BUILDING_CORRECTIONS[name]["year"]
                else:
                    year_text = cols[5].get_text(strip=True)
                    year_match = re.search(r'(19|20)\d{2}', year_text)
                    year = int(year_match.group(0)) if year_match else 0
                
                # Определение типа здания
                if 'башня' in name.lower() or 'tower' in name.lower():
                    building_type = "Башня"
                elif 'мост' in name.lower() or 'bridge' in name.lower():
                    building_type = "Мост"
                elif 'антенн' in name.lower():
                    building_type = "Телекоммуникационная вышка"
                else:
                    building_type = "Небоскреб"
                
                buildings.append({
                    'name': name,
                    'city': city,
                    'country': country,
                    'height': round(height, 1),
                    'year': year,
                    'type': building_type
                })
                
            except Exception as e:
                print(f"Пропущено здание {name}: {str(e)}")
                continue
        
        return buildings
    
    except Exception as e:
        print(f"Ошибка парсинга: {str(e)}")
        return []