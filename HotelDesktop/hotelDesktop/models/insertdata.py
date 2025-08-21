from hotelDesktop.appbackend.databaseconnect import SessionLocal
from hotelDesktop.models.models import Room, Guest, Booking
from datetime import date


session=SessionLocal()

def addrooms(numbers,room,prize,Status):
    room=Room(number=numbers,room_type=room,price=prize,status=Status)
    session.add(room)
    session.commit()
    session.close
    return 'done'

def addguests(name,phone,email):
    guest=Guest(name=name,phone=phone,email=email)
    session.add(guest)
    session.commit()
    session.close()
    return 'done'
    
def addbookings(room_id,guest_id,check_in,check_out,amount,paid):
    booking=Booking(room_id=room_id,guest_id=guest_id,check_in=check_in,check_out=check_out,amount=amount,paid=paid)
    session.add(booking)
    session.commit()
    session.close()
    return 'done'
    


    

room1=addrooms('101','Standard',2000000.00,'available')
room2=addrooms('102','Suite',45000.00,'available')
room3=addrooms('103','Deluxe',23334000.00,'available')
room4=addrooms('104','Suite',20040.00,'available')
room5=addrooms('105','Standard',34000.00,'available')


guest1=addguests('Terry Wisdom','09033819097','terrywisdom683@gmail.com')
guest2=addguests('Precious Kali','09122324097','preciouskali333@gmail.com')
guest3=addguests('Pixy Gee','09023423347','pixygee6423@gmail.com')
guest4=addguests('James Hardy','02023234242','jameshardy683@gmail.com')
guest5=addguests('Gilian Moore','04112312322','gilianmoore583@gmail.com')

booking1=addbookings(1,1,date(2022,3,3),date(2022,3,7),2000000.00,False)
booking2=addbookings(2,2,date(2022,5,3),date(2022,5,2),45000.00,True)
booking3=addbookings(3,3,date(2022,6,5),date(2022,3,3),23000000.00,False)
booking4=addbookings(4,4,date(2022,7,6),date(2022,3,3),300000.00,True)
booking5=addbookings(5,5,date(2022,8,7),date(2022,3,4),40000.00,False)