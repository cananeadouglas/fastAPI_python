from typing import List, Optional
from pydantic import BaseModel

class ItemUpdate(BaseModel):
    nome: Optional[str] = None
    carga: Optional[int] = None
    valor: Optional[int] = None
    finalizado: Optional[bool] = None
