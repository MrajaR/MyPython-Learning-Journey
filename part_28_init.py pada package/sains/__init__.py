# membuat folder package sains terkait langsung dengan modul pisika,
# sehingga jika nanti sains di import di file main.py, modul pisika bisa diakses/digunakan dengan cara seperti ini "sains.pisika...."
from . import pisika
#          yg diambil^



# membuat folder package sains terkait langsung dengan modul matematika
# sehingga jika nanti sains di import di file main.py, modul matematika bisa diakses/digunakan dengan cara seperti ini "sains.matematika"
from . import matematika
#            yg diambil^

# membuat folder package sains terkait langsung dengan function kali,
# sehingga jika nanti package sains diimport di file main.py. function kali di dalam file basic di package matematika --
# -- dapat langsung dipanggil/digunakan dengan sintaks pemanggilan "sains.kali"
from .matematika.basic import kali
#     yang dskip^          yg diambil^



# atau buat begini cara pengaitan yang lain (bisa beberapa atau semua modul/sub package yang dikaitkan *di contoh ini semuanya karena __all__)
# INI HANYA BERFUNGSI JIKA SINTAKS IMPORT DI FILE MAIN.PY SEPERTI "FROM PACKAGE IMPORT *"
# JIKA SINTAKS IMPORTNYA "IMPORT PACKAGE" MAKA TIDAK AKAN JALAN
# PENGAITAN SEPERTI INI JUGA TIDAK DISARANKAN
# __all__ = [
#     "matematika",
#     "pisika"
# ]