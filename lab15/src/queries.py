from typing import List, Optional
from .database import Database

class BuildingQueries:
    def __init__(self, db: Database):
        self.db = db
    
    def get_top_countries(self, limit: int = 5) -> Optional[List[tuple]]:
        query = """
        SELECT c.name, COUNT(b.id) as count
        FROM Buildings b
        JOIN Countries c ON b.country_id = c.id
        GROUP BY c.name
        ORDER BY count DESC
        LIMIT ?
        """
        return self.db.execute_query(query, (limit,))
    
    def get_total_height_top_n(self, n: int = 50) -> Optional[float]:
        query = """
        SELECT SUM(height)/1000 as total_km
        FROM (SELECT height FROM Buildings ORDER BY height DESC LIMIT ?)
        """
        result = self.db.execute_query(query, (n,))
        return result[0][0] if result else 0.0
    
    def get_tallest_buildings(self, limit: int = 5) -> Optional[List[tuple]]:
        query = """
        SELECT b.name, c.name, b.height, b.year, t.type_name
        FROM Buildings b
        JOIN Countries c ON b.country_id = c.id
        JOIN BuildingTypes t ON b.type_id = t.id
        ORDER BY b.height DESC
        LIMIT ?
        """
        return self.db.execute_query(query, (limit,))