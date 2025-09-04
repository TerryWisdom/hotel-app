from views.bookingView import booking
import customtkinter as ctk
import tkinter as tk
from datetime import date

class ScrollableFrame(ctk.CTkFrame):
    def __init__(self,master,*args,**kwargs):
        super().__init__(master,*args,**kwargs)
        
        #Canvas + scroolbar
       
        
        self.canvas=tk.Canvas(self,bg='white',highlightthickness=0)
        self.scrollbar=ctk.CTkScrollbar(self,orientation='vertical',command=self.canvas.yview)
        self.scrollbar.pack(side='right',fill='y')
        self.canvas.pack(fill='both',expand=True,padx=10,pady=0)

        
        #frame inside canvas
        self.scrollable_frame=ctk.CTkFrame(self.canvas,fg_color='white')
        self.scrollable_frame_id=self.canvas.create_window((0,0),window=self.scrollable_frame,anchor='nw')
        
        #Configure scroling
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame.bind('<Configure>',self._update_scrollregion)
        
        #mouse touchpad scrolling
        self.canvas.bind_all('<MouseWheel>',self._on_mousewheel)
        self.canvas.bind_all('<Button-4>',self._on_mousewheel)
        self.canvas.bind_all('<Button-5>',self._on_mousewheel)
        
                
        self.canvas.bind(
            '<Configure>',
            lambda e: self.canvas.itemconfig(
                self.scrollable_frame_id,width=e.width
            )
        )
        
    
    def _update_scrollregion(self,event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        self.canvas.yview_moveto(0)
        
        
    def _on_mousewheel(self, event):
        if event.delta:  # Windows/Linux
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif event.num == 4:  # macOS
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    def clear(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        

class BookingDisplay(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

       

        #Create the table frame
        table_frame = ctk.CTkFrame(self, )
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.labelFrame=ctk.CTkFrame(table_frame,corner_radius=0)
        self.labelFrame.pack(fill='x',pady=10,padx=(6,22))
        self.labelFrame.columnconfigure(0,weight=2)
        self.labelFrame.columnconfigure(1,weight=1)        
        
        self.Label=ctk.CTkLabel(self.labelFrame,text='Bookings',font=('Arial',22,'bold'),text_color='black')
        self.Label.pack(anchor='w',padx=10,pady=10)
        
        self.tabFram=ctk.CTkFrame(table_frame,fg_color='transparent',corner_radius=0)
        self.tabFram.pack(anchor='w',pady=10)
        self.tabs={
            'All Bookings':self.all_orders,
            'Filled Bookings':self.filled_orders,
            'Booking Orders':self.pending_orders     
        }
        
        
        tab_row = 1  

        # configure the table_frame grid so only col 0 grows, others don’t
        ''' for col in range(3):  # since you have 3 tabs
            table_frame.grid_columnconfigure(col, weight=0)

        # make sure the rest of the frame can expand but not the tab row
        table_frame.grid_columnconfigure(3, weight=1)  # empty space after tabs'''
                
        self.tab_labels={}#store references
        self.active_tab=None
        
        
        
        
        
        for i,( texts, func) in enumerate(self.tabs.items()):
                lbl=ctk.CTkLabel(self.tabFram,text=texts, fg_color='transparent',text_color='white',cursor='hand2',)
                lbl.grid(row=0,column=i,sticky='w',padx=15)
                
                lbl.bind('<Button-1>',lambda e,l=lbl,f=func: self.switch_tab(f,l))
                lbl.bind('<Enter>',lambda e,l=lbl: self.on_enter(e,l))
                lbl.bind('<Leave>',lambda e,l=lbl:self.on_leave(e,l))  
                self.tab_labels[texts] =lbl
        
        
         
        bookingheaderFrame=ctk.CTkFrame(table_frame,fg_color="#635353",corner_radius=0)
        bookingheaderFrame.pack(fill='x',padx=(6,22),pady=0)
        
        #bookingheaderFrame.columnconfigure(0,weight=2)
        #bookingheaderFrame.columnconfigure(1,weight=1)
        
        
        
        self.headers = ["GuestId", "RoomId", "RoomNo", "CheckIn","CheckOut","Price","Paid?"]
        for col in range(len(self.headers)):
            bookingheaderFrame.grid_columnconfigure(col,weight=1)
        #for header
        for col, text in enumerate(self.headers):
            lbl = ctk.CTkLabel(bookingheaderFrame, text=text, fg_color="#635353", width=100, height=30,font=('Arial',16,'bold'),text_color='white')
            lbl.grid(row=0, column=col, padx=1, pady=1, sticky="nsew")
            
        #Scrollable area
        self.scrollable=ScrollableFrame(table_frame)
        self.scrollable.pack(fill='both',expand='True')
        table_frame.grid_rowconfigure(2, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
       # table_frame.rowconfigure(2,weight=1)
        #table_frame.columnconfigure(0,weight=1)
        
        self.switch_tab(self.all_orders,self.tab_labels['All Bookings'])
        
        
       
        
        # Mouse wheel / touchpad scrolling

    def switch_tab(self,func,lbl):
        #reset all tabs to default
        for l in self.tab_labels.values():
            l.configure(text_color='white',font=('Arial',14))
            
        #Highlight active
        lbl.configure(text_color='red',font=('Arial',14,'bold'))
        
        #Highlight ative
        
        lbl.configure(text_color='red',font=('Arila',14,'bold'))
        self.active_tab=lbl
        
        #loadContent
        func()

   
   
    def on_enter(self, event, lbl):
        if lbl != self.active_tab:  # Only change if not active
            lbl.configure(text_color='lightgray')

    def on_leave(self, event, lbl):
        if lbl != self.active_tab:  # Reset if not active
            lbl.configure(text_color='white')

    # Tab contents
    def all_orders(self, event=None):
        self.scrollable.clear()        
        for row, record in enumerate(booking, start=1):
            dataColumnfram=ctk.CTkFrame(self.scrollable.scrollable_frame)
            dataColumnfram.pack(fill='x',padx=(6,22),pady=1)
            values = [record["guest_id"], record["room_id"], record["room_number"],
                      record["check_in"], record["check_out"],record["amount"],'Yes' if record["paid"] else 'No']
            for col, value in enumerate(values):
                cell = ctk.CTkLabel(dataColumnfram, text=value, fg_color="#444444", width=100, height=30,text_color='white')
                cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
                
            for col in range(len(values)):
                dataColumnfram.grid_columnconfigure(col, weight=1)


            
    def filled_orders(self, event=None):
        self.scrollable.clear()
        self.currentdate=date.today()
        for row,record in enumerate(booking, start=1):
            dataColumnfram=ctk.CTkFrame(self.scrollable.scrollable_frame)
            dataColumnfram.pack(fill='x',padx=(6,22),pady=1)
            if record['check_in'] < self.currentdate and record['check_out'] < self.currentdate:
                values = [record["guest_id"], record["room_id"], record["room_number"],
                    record["check_in"], record["check_out"],record["amount"],'Yes' if record["paid"] else 'No']  
                for col,value in enumerate(values):
                    cell=ctk.CTkLabel(dataColumnfram,text=value,fg_color="#444444",width=100, height=30,text_color='white')
                    cell.grid(row=row,column=col,padx=1,pady=1,stick='nswe')  
                    
                for col in range(len(values)):
                    dataColumnfram.grid_columnconfigure(col, weight=1)
            

    def pending_orders(self, event=None):
        self.scrollable.clear()
        for row, record in enumerate(booking,start=1):
            dataColumnfram=ctk.CTkFrame(self.scrollable.scrollable_frame)
            dataColumnfram.pack(fill='x',padx=(6,22),pady=1)
            if record['check_in']>self.currentdate and record['check_out']>self.currentdate:
                values = [record["guest_id"], record["room_id"], record["room_number"],
                record["check_in"], record["check_out"],record["amount"],'Yes' if record["paid"] else 'No']     
                for col,value in enumerate(values):
                    cell=ctk.CTkLabel(dataColumnfram,text=value,fg_color="#444444",width=100, height=30,text_color='white')
                    cell.grid(row=row,column=col,padx=1,pady=1,stick='nswe')  

                    dataColumnfram.grid_columnconfigure(col, weight=1)

                     
        

       