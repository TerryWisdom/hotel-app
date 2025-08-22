from sqlalchemy import Column,Integer,String, Date, ForeignKey, Float,Boolean
from appbackend.databaseconnect import Base, engine
from sqlalchemy.orm import relationship


class Guest(Base):
    __tablename__='guests'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    phone=Column(String)
    email=Column(String)
    bookings=relationship('Booking',back_populates='guest')
    

class Booking(Base):
    
    __tablename__='bookings'
    id=Column(Integer,primary_key=True,autoincrement=True)
    room_id=Column(Integer,ForeignKey('rooms.id'))
    guest_id=Column(Integer,ForeignKey('guests.id'))
    check_in=Column(Date,nullable=False)
    check_out=Column(Date,nullable=False)
    amount=Column(Float,default=0.0)
    paid=Column(Boolean,default=False)
    guest=relationship('Guest',back_populates='bookings')
    room=relationship('Room',back_populates='booking')
    
    
    
class Room(Base):
    __tablename__='rooms'
    id=Column(Integer,primary_key=True,autoincrement=True)
    number=Column(String,unique=True,nullable=False)
    room_type=Column(String,nullable=False)#Standard/Deluxe/suite
    price=Column(Float,nullable=False,default=0.0)
    status=Column(String,default='available')
    booking=relationship('Booking',back_populates='room')
    
    
Base.metadata.create_all(engine)