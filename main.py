import customtkinter as ctk
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SteganographyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Steganographer")
        self.geometry("500x400")

        self.navbar = ctk.CTkFrame(self)
        self.navbar.pack(side="top",fill="x")

        self.encode_button = ctk.CTkButton(self.navbar,text="Encode",command=self.show_encode_window)
        self.encode_button.pack(side="left",fill = "x",expand = True,padx=10,pady=10)
        
        self.decode_button = ctk.CTkButton(self.navbar,text="Decode",command=self.show_decode_window)
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

        self.encode_button = ctk.CTkButton(self.content_frame, text="Encode",command=self.encode_message)
        self.encode_button.pack(pady=10)


    def encode_image(self, image_path, message, output_path):
        img = Image.open(image_path)
        encoded_img = img.copy()
        width, height = img.size
        message += chr(0)  
        message_bits = ''.join(format(ord(char), '08b') for char in message)

        index = 0
        for y in range(height):
            for x in range(width):
                pixel = list(img.getpixel((x, y)))
                for n in range(3): 
                    if index < len(message_bits):
                        pixel[n] = pixel[n] & ~1 | int(message_bits[index])
                        index += 1
                encoded_img.putpixel((x, y), tuple(pixel))

        encoded_img.save(output_path)


    def encode_message(self):
        if hasattr(self,"image_path") and self.image_path:
            message = self.message_entry.get()
            if message:
                output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
                if output_path:
                    self.encode_image(self.image_path,message,output_path)
                    messagebox.showinfo("Success", "Message encoded successfully!")
            else:
                messagebox.showwarning("Input Error", "Please enter a message to encode.")
        else:
            messagebox.showwarning("Input Error", "Please select an image.")

    
    def show_decode_window(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.decode_label = ctk.CTkLabel(self.content_frame,text= "Decode Message from Image",font=("Arial",18,"bold"))
        self.decode_label.pack(pady=20)


        self.image_path_variable = StringVar()
        self.image_path_entry = ctk.CTkEntry(self.content_frame, width=300, placeholder_text="Enter the path of the image",textvariable=self.image_path_variable)
        self.image_path_entry.pack(pady=10)

        self.select_image_button = ctk.CTkButton(self.content_frame, text="Browse Image",command=self.browse_image)
        self.select_image_button.pack(pady=10)

        self.decode_button = ctk.CTkButton(self.content_frame, text="Decode", command=self.decode_message)
        self.decode_button.pack(pady=40)

        self.message_label = self.decode_label = ctk.CTkLabel(self.content_frame,text= "",font=("Arial",14,))
        self.message_label.pack(pady=0)

    def decode_message(self):
        if hasattr(self, 'image_path') and self.image_path:
            message = self.decode_image(self.image_path)
            if message:
                self.message_label.configure(text=message)
            else:
                messagebox.showwarning("Decode Error", "No message found or image is corrupted.")
        else:
            messagebox.showwarning("Input Error", "Please select an image.")

    def decode_image(self, image_path):
        img = Image.open(image_path)
        width, height = img.size
        message_bits = ''
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                for n in range(3):  
                    message_bits += str(pixel[n] & 1)

        message = ''
        for i in range(0, len(message_bits), 8):
            byte = message_bits[i:i+8]
            if byte == '00000000':  
                break
            message += chr(int(byte, 2))

        return message
if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()