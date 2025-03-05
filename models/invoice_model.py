from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class InvoiceItem(BaseModel):
    desc: str
    qty: float
    unitprice: float
    price: float

class Invoice(BaseModel):
    invoice_no: str
    invoice_datetime: datetime
    store_name: str
    store_address: str
    customer_name: str
    customer_info: Optional[str] = None #customer info is optional
    currency: str
    items: List[InvoiceItem]
    tax: float
    total: float
    discount: Optional[float] = None #discount is optional
    type: str #invoice type
    category: Optional[str] = None # category is optional