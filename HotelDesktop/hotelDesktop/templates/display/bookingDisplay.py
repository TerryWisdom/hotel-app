from views.bookingView import booking
import customtkinter as ctk
import tkinter as tk


  # 👈 your query function

class BookingDisplay(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # 1. Fetch data automatically
       # data =  booking  # 👈 assumes this returns list of tuples [(guestId, roomId, roomNo, checkin), ...]

        # 2. Create the table frame
        table_frame = ctk.CTkFrame(self, fg_color="#333333")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        

        
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
        
        """for row, record in enumerate(data, start=1):
            for col, value in enumerate(record):
                lbl = ctk.CTkLabel(inner_frame, text=value, fg_color="#444444", width=100, height=30)
                lbl.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")"""


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
