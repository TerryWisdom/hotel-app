from views.roomView import room
import customtkinter as ctk
from datetime import date
import tkinter as tk


class ScrollableFrame():
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
            columnHeader.grid(row=0,column=column, padx=50,pady=10 )
            
        self.canvas=ctk.CTkCanvas(self.mainframe)
        self.canvas.pack(side='left',fill='both',expand=True,padx=10,pady=0)
        self.scrollbar=ctk.CTkScrollbar(self.mainframe,orientation='vertical',command=self.canvas.yview)
        self.scrollbar.pack(side='left',fill='y')
        
        #frame inside the canvas
        
        self.scrollable_frame=ctk.CTkFrame(self.canvas,fg_color='skyblue')
        self.scrollable_frame_id=self.canvas.create_window((0,0),window=self.scrollable_frame,anchor='nw')
        
        #Configure scroling
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame.bind('<Configure>',self._update_scrollregion)
        
        #mouse touchpad scrolling
        self.canvas.bind_all('<MouseWheel>',self._on_mousewheel)
        self.canvas.bind_all('<Button-4>',self._on_mousewheel)
        self.canvas.bind_all('<Button-5>',self._on_mousewheel)
        
        
        
        for row, roominfo in enumerate(room,start=1):
            values=[roominfo['id'],roominfo['number'],roominfo['room_type'],roominfo['price'],roominfo['status'],['➕']]
            dataColumnfram=ctk.CTkFrame(self.scrollable_frame)
            dataColumnfram.pack(fill='x',padx=(6,22),pady=10)
            for col, value in enumerate(values):
                datainfo=ctk.CTkLabel(dataColumnfram,text=value,fg_color="#444444",text_color='white',font=('Arial',12,'bold'),width=70,height=30)
                datainfo.grid(row=0,column=col, padx=1, pady=1,sticky='nswe')
                    
            # make row columns expand evenly
            for col in range(len(values)):
                dataColumnfram.grid_columnconfigure(col, weight=1)
        
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
        