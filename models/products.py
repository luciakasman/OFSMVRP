from typing import List, Optional
from dataclasses import dataclass

@dataclass
class ProductData:
    sku: str
    name: Optional[str] = None
    weight_per_pallet: float

@dataclass
class Product:
    product_data: List[ProductData]