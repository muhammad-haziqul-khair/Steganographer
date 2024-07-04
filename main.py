import customtkinter as ctk
from tkinter import *
from tkinter import filedialog


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

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True)

        self.show_encode_window()

    def browse_image(self):
        self.image_path = filedialog.askopenfilename(title="Browse Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        self.image_path_variable.set(self.image_path)



    def show_encode_window(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.encode_label = ctk.CTkLabel(self.content_frame,text="Encode Message into Image",font=("Arial",18,"bold"))
        self.encode_label.pack(pady=20)

        self.image_path_variable = StringVar()
        self.image_path_entry = ctk.CTkEntry(self.content_frame, width=300, placeholder_text="Enter the path of the image",textvariable=self.image_path_variable)
        self.image_path_entry.pack(pady=10)

        self.select_image_button = ctk.CTkButton(self.content_frame, text="Browse Image",command=self.browse_image)
        self.select_image_button.pack(pady=10)


        self.message_entry = ctk.CTkEntry(self.content_frame, width=300, placeholder_text="Enter Message to Encode")
        self.message_entry.pack(pady=10)

        self.encode_button = ctk.CTkButton(self.content_frame, text="Encode")
        self.encode_button.pack(pady=10)





if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()