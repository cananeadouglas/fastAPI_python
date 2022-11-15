import sqlalchemy

from config import DATABASE_URL, metadata
from models.item import Item

def configurar_banco(databases_url = DATABASE_URL):
    print(databases_url)
    engine = sqlalchemy.create_engine(databases_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
if __name__ == "__main__":
    configurar_banco()

