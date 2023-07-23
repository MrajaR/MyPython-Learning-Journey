import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("600x300") # 600px x 300px
window.resizable(False,False) # false untuk x dan false untuk y
window.title("My First GUI") # judul

# frame input (pembuatan section layaknya div di html) menggunakan ttk
input_frame = ttk.Frame(window)


## memunculkan/menempatkan frame di window
# penempatan bisa menggunakan Grid,Pack,Place (disini menggunakan pack sehingga mengurut dari atas ke bawah atau dari kiri ke kanan tergantung argument fill nya)
# padx menambahkan padding ke arah x axis dan pady ke arah y axis
# fill='x' artinya menempatkan frame ke arah sumbu x, dan fill='y' menempatkan frame ke arah sumbu y
input_frame.pack(padx=10,pady=10,fill="x",expand=True)


NAMA_DEPAN = tk.StringVar() # membuat variabel untuk menangkap input dari nama depan, agar input dari nama depan tersimpan di variabel konstan NAMA_DEPAN
NAMA_BELAKANG= tk.StringVar() # membuat variabel untuk menangkap input dari nama belakang, agar input dari nama belakang tersimpan di variabel konstan NAMA_BELAKANG

## penempatan komponen-komponen ke dalam frame
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="First Name")
nama_depan_label.pack(padx=10,fill="x",expand=True)

# 2. entry/input untuk nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN) # konstan NAMA_DEPAN menjadi value dari argument text variabel agar input masuk ke konstan NAMA_DEPAN
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Last Name")
nama_belakang_label.pack(padx=10,fill="x",expand=True)

# 4. entry/input untuk nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG) # konstan NAMA_BELAKANG menjadi value dari argument text variabel agar input masuk ke konstan NAMA_BELAKANG
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

# 5. tombol
def button_click():
    '''this function is called by submit_button'''
    greeting = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Hope You're Doing Fine!!!"
    showinfo(title="Message For You", message=greeting)

submit_button = ttk.Button(input_frame, text='Send', command=button_click) # pemanggilan function sebagai value dari argument tidak menggunakan '()' dan argument functionnya 
submit_button.pack(fill='x', pady=10, padx=10, expand=True)

window.mainloop() # agar program bisa berjalan dengan menjadi infinite loop (akan berhenti jika kita close)
