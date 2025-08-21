from hotelDesktop.models.models import Room
from sqlalchemy.orm import sessionmaker
from hotelDesktop.appbackend.databaseconnect import SessionLocal

class GetRooms():
    
    def getRooms():
        session=SessionLocal()
        try:
            rooms=session.query(Room).all()
            return rooms
        finally:
            quit
            
    def to_string():
        room_list=[]
        for u in GetRooms.getRooms():
            room_dict={
                'id':u.id,
                'number':u.number,
                'room_type':u.room_type,
                'price':u.price,
                'status':u.status,
            }
            room_list.append(room_dict)
        return room_list
    
room=GetRooms.to_string()
