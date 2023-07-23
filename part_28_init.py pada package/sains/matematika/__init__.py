# mengaitkan sub package matematika dengan modul didalamnya yakni scientific dan basic
from . import basic,scientific

# mengaitkan sub package matematika dengan function tambah dan kali pada modul basic
# sehingga ketika dilakukan import "import sains",
# functionya dapat dipanggil dengan cara sains.matematika,tambah()
from .basic import tambah,kali
#  yg diskip^      yg diambil^

from .scientific import pangkat
#    yg diskip^      yg diambil^
