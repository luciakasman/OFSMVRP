from typing import List, Optional
from dataclasses import dataclass

@dataclass
class OrderData:
    order_id: str
    warehouse_id: str
    sku: str
    quantity_kg_liters: float
    customer_name: Optional[str] = None
    product_name: Optional[str] = None
    total_usd: Optional[float] = None
    pallets: float = 0

@dataclass
class AvailableVehiclesData:
    company_name: str
    SEMIS: int = 0
    BALANCIN: int = 0
    CHASIS_8TN: int = 0
    PICKUP_TRUCK: int = 0

@dataclass
class Orders:
    algorithm_type: str
    order_data: List[OrderData]
    available_vehicles: List[AvailableVehiclesData]
    max_distance: int = 2500