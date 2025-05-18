import pytest
from src.parser import parse_wikipedia_buildings

def test_parser_returns_list():
    """Проверяем, что парсер возвращает список"""
    result = parse_wikipedia_buildings()
    assert isinstance(result, list)

def test_parser_non_empty_result():
    """Проверяем, что парсер возвращает не пустой результат"""
    result = parse_wikipedia_buildings()
    assert len(result) > 0

def test_parser_data_structure():
    """Проверяем структуру возвращаемых данных"""
    result = parse_wikipedia_buildings()
    for item in result[:5]:  # Проверяем первые 5 элементов
        assert 'name' in item
        assert 'country' in item
        assert 'height' in item
        assert isinstance(item['height'], float)
        assert 'year' in item