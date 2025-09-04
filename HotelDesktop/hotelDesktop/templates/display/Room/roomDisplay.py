from views.roomView import room
import customtkinter as ctk
from datetime import date
import tkinter as tk


class ScrollableFrame():
    
    pass

class info_win(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        
        self.title('Book now')
        self.geometry('700x350')
        self.lift()
        self.focus_force()
        self.grab_set()
        self.resizable(False,False)
        
        self.roominfoframe=ctk.CTkFrame(self,corner_radius=0)
        self.roominfoframe.pack(fill='x')
        
        self.Bframe=ctk.CTkFrame(self,fg_color='transparent')
        self.Bframe.pack(fill='both',expand=True)
        self.content_frame=self.Guestui(self.Bframe)
        btnframe=ctk.CTkFrame(self,fg_color='transparent',corner_radius=0)
        btnframe.pack(fill='x')     
        btnframe.grid_columnconfigure(0,weight=2)   
        nextbtn=ctk.CTkButton(btnframe,text='Next',hover_color='#444444',command=lambda: self.GuestBookingUi(self.Bframe))
        nextbtn.pack(anchor='center',padx=(40,20),side='left',pady=(10,20))
        close_btn = ctk.CTkButton(btnframe, text="Close", command=self.destroy,fg_color='#635353')
        close_btn.pack(anchor='center',padx=(20,20),side='right',pady=(10,20))

        
        

        

    
    '''def clear_bframe(self):
        for widget in self.Bframe.winfo_children():
            widget.destroy()'''
    

    def Guestui(self,parent):
                
        guestinfoframe=ctk.CTkFrame(parent, corner_radius=0,fg_color='transparent')
        guestinfoframe.pack(fill='both',expand=True,ipadx=30)
        
        
        mainlabel=ctk.CTkLabel(guestinfoframe,text='Guest Info',font=('Arial',22,'bold'))
        mainlabel.grid(row=0,column=2,pady=(20,10))
        
        guestnameframe=ctk.CTkFrame(guestinfoframe, width=300,height=60,corner_radius=0)
        guestnameframe.grid(row=1,column=0,pady=(20,20),padx=(20,20))
        
        namelabel=ctk.CTkLabel( guestnameframe,text='Enter Name: ',font=('Arial',14,'bold'))
        namelabel.grid(row=0,column=0,padx=10)        
        nameInput=ctk.CTkEntry(guestnameframe,width=200,height=30,corner_radius=0,placeholder_text='enter name')
        nameInput.grid(row=0,column=1)
        
        
        guestphoneframe=ctk.CTkFrame(guestinfoframe,width=300,height=60,corner_radius=0)
        guestphoneframe.grid(row=1,column=2,pady=(20,20),padx=10)
        phonelabel=ctk.CTkLabel(guestphoneframe,text='Phone: ',font=('Arial',14,'bold'))
        phonelabel.grid(row=0,column=1,padx=10)
        phoneInput=ctk.CTkEntry(guestphoneframe,width=200,height=30,corner_radius=0,placeholder_text='enter phone number')
        phoneInput.grid(row=0,column=2)
        
        guestemailframe=ctk.CTkFrame(guestinfoframe,width=300,height=60,corner_radius=0)
        guestemailframe.grid(row=2,columnspan=3,padx=(20,10))
        emailabel=ctk.CTkLabel(guestemailframe,text='Email: ',font=('Arial',14,'bold'))
        emailabel.grid(row=0,column=0,padx=10)
        emailinput=ctk.CTkEntry(guestemailframe,placeholder_text='enter your emial',width=200,height=30,corner_radius=0)
        emailinput.grid(row=0,column=2)   
            
    def GuestBookingUi(self):
        pass        
            



class RoomDisplay(ctk.CTkFrame):
    def __init__(self,master,*args,**kwargs):
        super().__init__(master,*args,**kwargs)
        
        self.mainframe=ctk.CTkFrame(self)
        self.mainframe.pack(fill='both',expand=True,padx=10,pady=10)
        
        headerFrame=(ctk.CTkFrame(self.mainframe,corner_radius=0))
        headerFrame.pack(fill='x',padx=(6,22),pady=10)
        
        headerFrame.columnconfigure(0,weight=2)
        headerFrame.columnconfigure(1,weight=1)
        
        roomHeader=ctk.CTkLabel(headerFrame,text='ROOMS',font=('Arial',22,'bold'),text_color='black')
        roomHeader.grid(row=0,column=0,sticky='w',padx=10,pady=10)
        
        addroomsBtn=ctk.CTkButton(headerFrame,text='➕AddRooms',text_color='black',width=40,height=40,corner_radius=0,fg_color='transparent',hover=False,font=('arial',14,'bold'))
        addroomsBtn.grid(row=0,column=1,sticky='e',padx=(10,10))
        
        addroomsBtn.bind('<Enter>',lambda e :addroomsBtn.configure(text_color='gray'))
        addroomsBtn.bind('<Leave>',lambda e :addroomsBtn.configure(text_color='black'))
        
        
        #ColumsHEader
        
        columnsHeaderFrame=ctk.CTkFrame(self.mainframe,fg_color='#635353',corner_radius=0)
        columnsHeaderFrame.pack(fill='x',padx=(6,22),pady=0)
        

        
        roomcolumns=['id','number','room_type','price','status','Book']
        
        for column,col in enumerate(roomcolumns):
            columnHeader=ctk.CTkLabel(columnsHeaderFrame,text=col,text_color='white',font=('Arial',16,'bold'),width=70,height=30)
            columnHeader.grid(row=0,column=column, padx=1,pady=10,sticky='nswe' )
            
        for col in range(len(roomcolumns)):
            columnsHeaderFrame.grid_columnconfigure(col,weight=1)
                        
        self.canvas=ctk.CTkCanvas(self.mainframe)
        self.scrollbar=ctk.CTkScrollbar(self.mainframe,orientation='vertical',command=self.canvas.yview)
        self.scrollbar.pack(side='right',fill='y')
        self.canvas.pack(fill='both',expand=True,padx=10,pady=0)

        
        #frame inside the canvas
        
        self.scrollable_frame=ctk.CTkFrame(self.canvas,fg_color='transparent')
        self.scrollable_frame_id=self.canvas.create_window((0,0),window=self.scrollable_frame,anchor='nw')
        
        #Configure scroling
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame.bind('<Configure>',self._update_scrollregion)
        
        self.canvas.bind(
            '<Configure>',
            lambda e: self.canvas.itemconfig(
                self.scrollable_frame_id,width=e.width
            )
        )
        
        #mouse touchpad scrolling
        self.canvas.bind_all('<MouseWheel>',self._on_mousewheel)
        self.canvas.bind_all('<Button-4>',self._on_mousewheel)
        self.canvas.bind_all('<Button-5>',self._on_mousewheel)
        
        
        
        for row, roominfo in enumerate(room,start=1):
            values=[roominfo['id'],roominfo['number'],roominfo['room_type'],roominfo['price'],roominfo['status'],['➕']]
            dataColumnfram=ctk.CTkFrame(self.scrollable_frame)
            dataColumnfram.pack(fill='x',padx=(6,22),pady=1)
            for col, value in enumerate(values):
                datainfo=ctk.CTkLabel(dataColumnfram,text=value,fg_color="#444444",text_color='white',font=('Arial',12,'bold'),width=70,height=30)
                datainfo.grid(row=0,column=col, padx=1, pady=1,sticky='nswe')
                    
            # make row columns expand evenly
            for col in range(len(values)):
                dataColumnfram.grid_columnconfigure(col, weight=1)
                
                if col == len(values)-1:
                    datainfo.bind(
                        '<Button-1>',
                        lambda e, v=values: self.addBooking(v)
                    )
                    
                    
        
                    
    def addBooking(self,row_values):
        self.Booknow=info_win(self)
        labels=['Room Id','Number','Type','price','Status']
        
        #roominfoFram=ctk.CTkFrame(self.Booknow.roominfoframe,corner_radius=0)
       # roominfoFram.pack(fill='x')
       
        for i,(label,value)in enumerate(zip(labels,row_values[:-1])):
            lbl=ctk.CTkLabel(self.Booknow.roominfoframe, text=f'{label}: {value}',font=('Arial',14))
            lbl.grid(row=0,column=i,padx=10,pady=10,sticky='nsew')
            
            
        
            self.Booknow.roominfoframe.grid_columnconfigure(i,weight=2)

        # Add Guest ui   

        
        
        
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
        