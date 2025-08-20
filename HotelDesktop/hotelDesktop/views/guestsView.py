from hotelDesktop.models.models import Guest
from sqlalchemy.orm import sessionmaker
from hotelDesktop.appbackend.databaseconnect import SessionLocal

class GetGuest():
    
    def getGuest():
        session=SessionLocal()
        try:
            guest=session.query(Guest).all()
            return guest
        finally:
            session.close()
            
    def to_string():
        guest_list=[]
        for u in GetGuest.getGuest():
            guest_dict={
                'id':u.id,
                'name':u.name,
                'phone':u.phone,
                'email':u.email,
                
            }
            guest_list.append(guest_dict)
        return guest_list
    
guest=GetGuest.to_string()
print(guest)