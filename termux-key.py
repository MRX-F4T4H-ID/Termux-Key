import os
from time import sleep

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print('''
 _____ _____ ____  __  __ _   ___  __     _  _________   __
|_   _| ____|  _ \|  \/  | | | \ \/ /    | |/ / ____\ \ / /
  | | |  _| | |_) | |\/| | | | |\  /_____| ' /|  _|  \ V /
  | | | |___|  _ <| |  | | |_| |/  \_____| . \| |___  | |
  |_| |_____|_| \_\_|  |_|\___//_/\_\    |_|\_\_____| |_| ''')
print(a+'_'*70)
print('\nProses..')
sleep(1)
print(b+'\n[-] Membuat folder termux properties...')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[+]Success !')
sleep(1)
print(b+'\n[-] Membuat file pengaturan............')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
amjeng = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
amjeng.write(key)
amjeng.close()
sleep(1)
print(a+'[+] Success !')
sleep(1)
print(b+'\n[-] Pengaturan--->')
sleep(2)
os.system('termux-reload-settings')
print(a+'[+] Succes !'+c+'\n\nTERIMA KASIH SUDAH MENGINSTALL:)\n\n')
print(a+'_'*70)
