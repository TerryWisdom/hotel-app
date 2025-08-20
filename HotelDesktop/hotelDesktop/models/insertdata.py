from appbackend.databaseconnect import SessionLocal
from .models import Room

session=SessionLocal()

def addrooms(number,room_type,price,status,booking):
    room=Room(number,room_type,price,status,booking)
    
    session.add_all(room)
    session.commit()
    session.close
    return 'done'
    
    

room1=addrooms('101','Standard',2000000.00,'available','Booking')
room2=addrooms('102','Suite',45000.00,'available','Booking')
room3=addrooms('103','Deluxe',23334000.00,'available','Booking')
room4=addrooms('104','Suite',20040.00,'available','Booking')
room5=addrooms('105','Standard',34000.00,'available','Booking')

