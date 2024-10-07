from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Corrige a URL de conexão usando pymysql
db = 'mysql+pymysql://root:1103@localhost:3306/logincli'
engine = create_engine(db, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email =  Column(String(200))
    pwd = Column(String(100))
    
Base.metadata.create_all(engine)
