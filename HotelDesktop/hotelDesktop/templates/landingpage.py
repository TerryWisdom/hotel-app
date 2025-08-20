import customtkinter as ctk



class LandingPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        #app setup
        self.title('Hotel Management')
        self.geometry('1000x600')
        
        
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
        buttons=['Dashboard','Rooms','Booking','Guests','Reports']
        button_frame=ctk.CTkFrame(self.sidebar,fg_color='transparent')
        button_frame.pack(expand=True)
        
        for btn in buttons:
            button=ctk.CTkButton(button_frame,text=btn,
                                 width=186,height=47, fg_color='#635353',
                                 corner_radius=10,command=lambda name=btn: self.show_page(name),text_color='white',hover_color='#534343')
            button.pack(pady=10,padx=20,fill='x')
        
        #main content area
        self.main_content=ctk.CTkFrame(self,corner_radius=15,fg_color='#635353')
        self.main_content.grid(row=0,column=1,sticky='nswe',padx=10,pady=10)
        
        self.label=ctk.CTkLabel(self.main_content,text='Welcome to Hotel Management System',
                                font=('Arial',20),text_color='black')
        self.label.pack(pady=20)
            
        
        

if __name__=='__main__':
    app=LandingPage()
    app.mainloop()