from gtts import gTTS
import os

os.system("apt-get install python")
           
os.system("apt-get install figlet")

os.system("clear")

os.system("figlet YUBA ^^")

banner = """
                             >Coder By Yuba
|> tiktok= yuba0
|> github = github.com/yuba-0/
"""

print(banner)



while(True):
     istenilen = input('Söylemek istediğiniz şeyi giriniz:')
     say = gTTS(text= istenilen, lang = 'tr')
     say.save('isim.wav')
     os.system('isim.wav')
