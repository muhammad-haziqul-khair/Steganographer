import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SteganographyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Steganographer")
        self.geometry("500x400")

        self.navbar = ctk.CTkFrame(self)
        self.navbar.pack(side="top",fill="x")

        self.encode_button = ctk.CTkButton(self.navbar,text="Encode")
        self.encode_button.pack(side="left",fill = "x",expand = True,padx=10,pady=10)
        
        self.decode_button = ctk.CTkButton(self.navbar,text="Decode")
        self.decode_button.pack(side="left",fill = "x",expand = True,padx=10,pady=10)




if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()