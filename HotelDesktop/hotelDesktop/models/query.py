from appbackend.databaseconnect import SessionLocal
from models.models import Room, Guest, Booking
from datetime import date


session=SessionLocal()

user=session.query(Guest).all()#.filter_by(name='Terry Wisdom').first()
booking=[]
for i in user:
    if i.bookings:
        for j in i.bookings:
            users=i.id,i.name,i.phone,j.room.id,j.room.number,j.room.room_type,j.paid,j.check_in,j.check_out
            booking.append(users)
    
print(booking)
    
