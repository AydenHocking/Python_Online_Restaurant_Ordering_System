from typing import List, Optional
from pydantic import BaseModel
# from .ingredients import Ingredient
from .orderitem import OrderItem

class MenuItemBase(BaseModel):
    name: str
    price: float
    description: str
    calories: int
    category: str

class MenuItemCreate(MenuItemBase):
    pass
class MenuItemUpdate(BaseModel):

    calories: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int
    orderitem: Optional[OrderItem] = None


    class ConfigDict:
        from_attributes = True