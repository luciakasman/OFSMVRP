
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class ClientData:
    warehouse_id: str
    client_name: str
    address: Optional[str] = None
    locality: Optional[str] = None
    province: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

@dataclass
class Client:
    client_data: List[ClientData]