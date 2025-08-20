from models.models import Room
from sqlalchemy.orm import sessionmaker
from appbackend.databaseconnect import SessionLocal

class GetRooms():
    
    def getRooms():
        session=SessionLocal()
        try:
            rooms=session.query(Room).all()
            return rooms
        finally:
            session.close()
            
    def to_string():
        for u in GetRooms.getRooms():
            rooms={
                'id':u.id,
                'name':u.name,
                'email':u.email
            }
        return rooms
    
    
