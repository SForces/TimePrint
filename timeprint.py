import time
import sys

def Timeprint(saniye, metin):
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(int(saniye)/len(metin))
    print(""
    
   
