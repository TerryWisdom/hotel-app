from models.models import Guest
from sqlalchemy.orm import sessionmaker
from appbackend.databaseconnect import SessionLocal

class GetGuest():
    
    def getGuest():
        session=SessionLocal()
        try:
            guest=session.query(Guest).all()
            return guest
        finally:
            quit
            
    def to_string():
        guest_list=[]
        for guest in GetGuest.getGuest():
            if guest.bookings:
                for booking in guest.bookings:
                    guest_dict={
                        'id':guest.id,
                        'name':guest.name,
                        'phone':guest.phone,
                        'email':guest.email,
                        'room':booking.room.number,
                        'room_id':booking.room.id,
                        'check_in':booking.check_in,
                        'check_out':booking.check_out,
                        
                    }
            guest_list.append(guest_dict)
        return guest_list
    
guest=GetGuest.to_string()
