from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:909144002@localhost/pay_system")
sessionlocal = sessionmaker(bind=engine)
Base = declarative_base()

# генетратор соединений
def get_db():
    db = sessionlocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

from database import models