from views.bookingView import booking
import customtkinter as ctk
import tkinter as tk


class ScrollableFrame(ctk.CTkFrame):
    def __init__(self,master,*args,**kwargs):
        super().__init__(master,*args,**kwargs)
        
        #Canvas + scroolbar
        
        bookingheaderFrame=ctk.CTkFrame(self,fg_color="#635353",width=300,height=30,corner_radius=0)
        bookingheaderFrame.pack(fill='x')
        
        headers = ["GuestId", "RoomId", "RoomNo", "CheckIn","CheckOut","Price","Paid?"]
        #for header
        for col, text in enumerate(headers):
            lbl = ctk.CTkLabel(bookingheaderFrame, text=text, fg_color="#635353", width=100, height=30,font=('Arial',16,'bold'),text_color='white')
            lbl.grid(row=1, column=col, padx=1, pady=1, sticky="nsew")
        
        self.canvas=tk.Canvas(self,bg='white',highlightthickness=0)
        self.scrollbar=ctk.CTkScrollbar(self,orientation='vertical',command=self.canvas.yview)
        self.scrollbar.pack(side='left',fill='y')
        self.canvas.pack(side='left',fill='both',expand=True)
        
        
        #frame inside canvas
        self.scrollable_frame=ctk.CTkFrame(self.canvas,fg_color='white')
        self.scrollable_frame_id=self.canvas.create_window((0,0),window=self.scrollable_frame,anchor='nw')
        
        #Configure scroling
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame.bind('<Configure>',lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        
        #mouse touchpad scrolling
        self.canvas.bind_all('<MouseWheel>',self._on_mousewheel)
        self.canvas.bind_all('<Button-4>',self._on_mousewheel)
        self.canvas.bind_all('<Button-5>',self._on_mousewheel)
        
        
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
        table_frame = ctk.CTkFrame(self, fg_color="#333333")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        

        self.Label=ctk.CTkLabel(table_frame,text='Bookings',font=('Arial',22,'bold'),text_color='white')
        self.Label.pack(anchor='w')
        
        self.tabFram=ctk.CTkFrame(table_frame,fg_color='transparent')
        self.tabFram.pack(anchor='w')
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
            values = [record["guest_id"], record["room_id"], record["room_number"],
                      record["check_in"], record["check_out"],record["amount"],'Yes' if record["paid"] else 'No']
            for col, value in enumerate(values):
                cell = ctk.CTkLabel(self.scrollable.scrollable_frame, text=value, fg_color="#444444", width=100, height=30)
                cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")


            
    def filled_orders(self, event=None):
        self.scrollable.clear()
        for i in range(10):
            lbl = ctk.CTkLabel(self.scrollable.scrollable_frame, text=f"Filled {i+1}", text_color="green")
            lbl.pack(anchor="w", padx=10, pady=5)
            

    def pending_orders(self, event=None):
        self.scrollable.clear()
        for i in range(5):
            lbl = ctk.CTkLabel(self.scrollable.scrollable_frame, text=f"Pending {i+1}", text_color="orange")
            lbl.pack(anchor="w", padx=10, pady=5)

        """
        headLabel=ctk.CTkLabel(table_frame,text='BOOKINGS',font=('Arial',22,'bold'),text_color='white')
        headLabel.pack()
        bookingheaderFrame=ctk.CTkFrame(table_frame,fg_color="#635353",width=300,height=30)
        bookingheaderFrame.pack()
        # 3. Create canvas + scrollbar
        canvas = tk.Canvas(bookingheaderFrame, bg="#333333", highlightthickness=0)
        canvas.grid(row=1,column=0,padx=1,pady=1,sticky='nswe',columnspan=7)

        scrollbar = ctk.CTkScrollbar(table_frame, orientation="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # 4. Inner frame inside canvas
        inner_frame = ctk.CTkFrame(canvas, fg_color="#333333")
        canvas.create_window((0, 0), window=inner_frame, anchor="center")

        # 5. Update scroll region
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        inner_frame.bind("<Configure>", on_frame_configure)
        
        


        # 6. Create table headers
        headers = ["GuestId", "RoomId", "RoomNo", "CheckIn","CheckOut","Price","Paid?"]
        for col, text in enumerate(headers):
            lbl = ctk.CTkLabel(bookingheaderFrame, text=text, fg_color="#635353", width=100, height=30,font=('Arial',16,'bold'),text_color='white')
            lbl.grid(row=0, column=col, padx=1, pady=1, sticky="nsew")

        # 7. Fill rows
        for row, record in enumerate(booking, start=1):
            values = [record["guest_id"], record["room_id"], record["room_number"],
                      record["check_in"], record["check_out"],record["amount"],'Yes' if record["paid"] else 'No']
            for col, value in enumerate(values):
                cell = ctk.CTkLabel(inner_frame, text=value, fg_color="#444444", width=100, height=30)
                cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        
        '''for row, record in enumerate(data, start=1):
            for col, value in enumerate(record):
                lbl = ctk.CTkLabel(inner_frame, text=value, fg_color="#444444", width=100, height=30)
                lbl.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")'''
        """


'''class BookingDisplay(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Table frame inside BookingDisplay
        table_frame = ctk.CTkFrame(self, fg_color='#333333')
        table_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Configure grid expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Canvas for scrollable area
        canvas = tk.Canvas(table_frame, bg="#d9d9d9", highlightthickness=0)
        canvas.grid(row=0, column=0, sticky="nsew",)

        scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Inner frame inside canvas
        inner_frame = ctk.CTkFrame(canvas, fg_color="transparent")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        

        # Update scrollregion when inner_frame resizes
        inner_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # === Headers ===
        headers = ["GuestId", "RoomId", "RoomNo", "CheckIn", "CheckOut", "Amount", "Paid"]
        for j, header in enumerate(headers):
            h = ctk.CTkLabel(inner_frame, text=header, fg_color="#635353", text_color="white",
                             font=("Arial", 14, "bold"))
            h.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")

        # === Data rows ===
        for i, row in enumerate(booking, start=1):
            values = [row["guest_id"], row["room_id"], row["room_number"],
                      row["check_in"], row["check_out"], row["amount"], row["paid"]]
            for j, value in enumerate(values):
                cell = ctk.CTkLabel(inner_frame, text=value, anchor="w")
                cell.grid(row=i, column=j, padx=5, pady=2, sticky="nsew")

        # Stretch columns
        for j in range(len(headers)):
            inner_frame.grid_columnconfigure(j, weight=1)'''
