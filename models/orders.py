
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class OrderData:
    order_id: str
    id_deposito: str
    sku: str
    cantidad_kg_litros: float
    nombre_cliente: Optional[str] = None
    nombre_producto: Optional[str] = None
    total_usd: Optional[float] = None
    pallets: float = 0

@dataclass
class AvailableVehiclesData:
    nombre_empresa: str
    SEMIS: int = 0
    BALANCIN: int = 0
    CHASIS_8TN: int = 0
    CAMIONETA: int = 0

@dataclass
class Orders:
    user_id: str
    organization_id: str
    algorithm_type: str
    order_data: List[OrderData]
    available_vehicles: List[AvailableVehiclesData]
    max_distance: int = 2500