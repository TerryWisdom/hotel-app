from hotelDesktop.models.models import Booking
from sqlalchemy.orm import sessionmaker
from hotelDesktop.appbackend.databaseconnect import SessionLocal
from datetime import time

class GetBookings():
    
    def getbookings():
        session=SessionLocal()
        try:
            booking=session.query(Booking).all()
            return booking
        finally:
            quit
            
    def to_string():
        booking_list=[]
        for u in GetBookings.getbookings():
            
            booking_dict={
                'room_id':u.room_id,
                'room_number':u.room.number,
                'guest_id':u.guest_id,
                'check_in':u.check_in,
                'check_out':u.check_out,
                'amount':u.amount,
                'paid':u.paid
                
            }
            booking_list.append(booking_dict)
        return booking_list
    
booking=GetBookings.to_string()
