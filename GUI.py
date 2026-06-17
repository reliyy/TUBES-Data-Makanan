import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# 1. Membuat jendela utama dengan tema modern (contoh: 'darkly' atau 'flatly')
app = ttk.Window(themename="vapor")
app.title("Aplikasi Stok Makanan")
app.geometry("600x500")

# 2. Membuat komponen teks (Label)
label = ttk.Label(
    app, 
    text="Button", 
    font=("Helvetica", 14), 
    bootstyle="primary"
)
label.pack(pady=20)

# Fungsi yang akan jalan kalau tombol diklik
def tombol_diklik():
    label.config(text="Tombol berhasil diklik! ", bootstyle="success")

# 3. Membuat Tombol (Button)
tombol = ttk.Button(
    app, 
    text="Lanjut", 
    bootstyle="success", 
    command=tombol_diklik
)
tombol.pack(pady=10)

# 4. Menjalankan aplikasi
app.mainloop()