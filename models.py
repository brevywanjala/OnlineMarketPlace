from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey,Float,Date
from sqlalchemy.orm import sessionmaker, relationship ,foreign
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date


Base = declarative_base()
db_url = 'sqlite:///market_store.db'

# db_url='postgresql://postgres:3tFayHEBlQB6BNyoM6gc@containers-us-west-69.railway.app:7261/railway'
engine = create_engine(db_url , echo=True,pool_size=20, max_overflow=30)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username=Column(Integer)# Add user-related fields (e.g., name, email, password, etc.)
    email = Column(String(20),unique=True)  # 'teacher' or 'parent'
    phone= Column(String(255))
    password=Column(String(255))
    usertype=Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)
    
class Item(Base):
    __tablename__ ="items"
    id = Column(Integer, primary_key=True)
    item_name =Column(String(255))
    img= Column(String(255))
    description= Column (String(255))
    quantity= Column (Integer)
    amount=Column(Float)
    category_id = Column (String(255) ,ForeignKey("categories.id"),default=1)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer,ForeignKey("users.id"))
    
    



class  Category(Base):
    __tablename__ ="categories"
    id = Column(Integer, primary_key=True)
    name =Column(String(255))  
      
class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    amount =Column(Float)
    item_id=Column(Integer,ForeignKey("items.id"))
    method= Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)
     
    
    
    
    



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()