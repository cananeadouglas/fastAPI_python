import ormar
#import re
#from pydantic import validator
from config import database, metadata


class Item(ormar.Model):
    
    class Meta:
        metadata = metadata
        database = database
        tablename = "items"
    
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    carga: int = ormar.Integer()
    valor: float = ormar.Float()
    finalizado: bool = ormar.Boolean(default=False)
    
    #@validator('nome')
    #def valida_valor(cls, v):
    #    if re.compile('^[A-Z]{4}[0-9]{1,2}$').match(v):
    #        raise ValueError('o Valor está errado, formato')
    #    else:
    #        return v
    
        



