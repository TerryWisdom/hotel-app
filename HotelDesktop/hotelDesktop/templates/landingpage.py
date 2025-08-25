import customtkinter as ctk
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class LandingPage(ctk.CTk):
    tools=[{'fgcolor':'#635353'}]
    
    
    def __init__(self):
        super().__init__()
        
        

        #app setup
        self.title('Hotel Management')
        self.geometry('1024x600')
        
        
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')
        #635353
        #Configure grid
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        
        #sidebar
        self.sidebar=ctk.CTkFrame(self,width=210,corner_radius=15,fg_color='#635353')
        self.sidebar.grid(row=0,column=0,sticky='ns',padx=10,pady=10)
        
        #sideButtons
        self.buttons={'Dashboard':self.open_dashboard,
                      'Rooms':self.open_rooms,
                      'Booking':self.open_booking,
                      'Guests':self.open_guest,
                      'Reports':self.open_reports
                    }
        
        button_frame=ctk.CTkFrame(self.sidebar,fg_color='transparent')
        button_frame.pack(expand=True)
        

        #main content area
        self.main_content=ctk.CTkFrame(self,corner_radius=15,fg_color='#635353')
        self.main_content.grid(row=0,column=1,sticky='nswe',padx=10,pady=10)
        
        self.label=ctk.CTkLabel(self.main_content,text='Welcome to Hotel Management System',
                                font=('Arial',20),text_color='black')
        self.label.pack(pady=20)
        
        for btn, command in self.buttons.items():
            button=ctk.CTkButton(button_frame,text=btn,
                                 width=186,height=47, fg_color='#635353',
                                 corner_radius=10,command=command,text_color='white',hover_color='#534343')
            button.pack(pady=10,padx=20,fill='x')
        
        self.content_frame=None
        
    
    
    def open_dashboard(self):
        print('hi')
        from templates.display.Dashboard import dashBoardDisplay
        dashBoardDisplay(self)
    
    def open_guest(self):
        print('hi')
        from templates.display.Guest import guestDisplay
        guestDisplay(self)
    
    def open_booking(self):
        
        from templates.display.Booking.bookingDisplay import BookingDisplay
        self.content_frame=BookingDisplay(self)
        self.content_frame.grid(row=0,column=1,sticky='nsew')
        #self.rowconfigure(0,weight=1)
        #self.columnconfigure(0,weight=1)
    
    def open_rooms(self):
        print('hi')
        from templates.display.Room import roomDisplay
        roomDisplay(self)
    
    def open_reports(self):
        print('hi')
        from templates.display.Report import reportDisplay
        reportDisplay(self)
        
        

if __name__=='__main__':
    app=LandingPage()
    app.mainloop()