from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Depot:
    warehouse_id: str
    warehouse_name: str
    address: Optional[str] = None
    locality: Optional[str] = None
    province: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
