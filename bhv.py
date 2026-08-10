																		
#Modüller
import pyfiglet
import os
import time

#Renkler
KIRMIZI = "\033[91m"
YESIL   = "\033[92m"
SARI    = "\033[93m"
MAVI    = "\033[94m"
MOR     = "\033[95m"
CYAN    = "\033[96m"
BEYAZ   = "\033[97m"
GRI     = "\033[90m"
RESET   = "\033[0m"

#giriş
os.system("pkg update && pkg upgrade -y")
os.system("pkg install git -y")
os.system("clear")
print("bitmek üzere...")
time.sleep(3)
os.system("clear")
print("Bitti!")
time.sleep(1.5)
os.system("clear")

#Menü
def menu():
	yazi = pyfiglet.figlet_format("BHVx777")
	print(f"{MAVI}{yazi}{RESET}")
	print(f"""{YESIL}Mehraba BHV'ye hoşgeldiniz burda bir çok Rat bulunmaktadır istediğiniz RAT'ı seçin{RESET}""")
	print(f"""{YESIL}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■{RESET}""")
	print(f"{BEYAZ}Geliştirici: {MOR}VHG{RESET}")
	print(f"{YESIL}istediğiniz Rat'ı sayı ile belitriniz{RESET}")
	print(f"{YESIL}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■{RESET}")
	print(f"{KIRMIZI}[1]{RESET}	{CYAN}ModulerStegoRAT{RESET}")
	print(f"{KIRMIZI}[2]{RESET}	{CYAN}Remote-acces-trojan{RESET}")
	print(f"{KIRMIZI}[3]{RESET}	{CYAN}PhantomLink{RESET}")
	print(f"{KIRMIZI}[4]{RESET}	{CYAN}DBsploit{RESET}")
	print(f"{KIRMIZI}[5]{RESET}	{CYAN}Discord-Remote-Access-Tool{RESET}")
	print(f"{KIRMIZI}[6]{RESET}	{CYAN}jarbou3{RESET}")
	print(f"{KIRMIZI}[7]{RESET}	{CYAN}Trojan-python{RESET}")
	print(f"{KIRMIZI}[8]{RESET}	{CYAN}Lo4bf-Malware{RESET}")
	print(f"{KIRMIZI}[9]{RESET}	{CYAN}PIRATE{RESET}") #KORSAN
	print(f"{KIRMIZI}[10]{RESET}	{CYAN}RSB-FRAMEWORK{RESET}")
	print(f"{KIRMIZI}[11]{RESET}	{CYAN}Kizagan{RESET}") #ya olm o ASCII banner şeyini nasıl yapiyorsunuz aq
	print(f"{KIRMIZI}[12]{RESET}	{CYAN}thorse{RESET}")
	print(f"{KIRMIZI}[99]   	Exit{RESET}")
	print(f"{YESIL}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■{RESET}")

#kök
while True:
	menu()
	secim = input(f"{SARI}Seçiminizi giriniz:	{RESET}")
	if secim == "1":
		os.system("git clone https://github.com/RaspiestSheep3/ModularStegoRAT.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim ==  "2":
		os.system("git clone https://github.com/KoushikReddy9963/Remote-access-trojan.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system*"clear")
	elif secim == "3":
		os.system("git clone http]]s://github.com/AhmadMAnis/PhantomLink.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "4":
		os.system("git clone https://github.com/b3d3c/BDsploit.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "5":
		os.system("git clone https://github.com/jluotosun/Discord-Remote-Access-Tool.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear"(
	elif secim == "6":
		os.system("git clone https://github.com/TheNewAttacker64/jarbou3.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "7":
		os.system("git clone https://github.com/zedxpace/Trojan-in-Python.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "8":
		os.system("git clone https://github.com/loafiieee/Lo4f-Malware.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "9":
		os.system("git clone https://github.com/gbrn1/PIRATE.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "10":
		os.system("git clone https://github.com/tarcisio-marinho/RSB-Framework.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "11":
		os.system("git clone https://github.com/st4inl3s5/kizagan.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "12":
		os.system("git clone https://github.com/PushpenderIndia/thorse.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "14":
		os.system("git clone https://github.com/Viralmaniar/Powershell-RAT.git")
		input(f"{SARI}Tool'unuz RAT adlı klasörünüze yüklendi devam etmek için Enter tıklayın...{RESET}")
		os.system("clear")
	elif secim == "99":
	     print(f"{KIRMIZI}Çıkılıyor...{RESET}")
	     time.sleep(3)
	     print(f"{SARI}BHV sizi tekrar bekler >:){RESET}")
	     time.sleep(1.5)
	     os.system("cd")
	     os.system("clear")
	     break
	else:
	    print(f"{KIRMIZI}Yanlış seçim{RESET}")
	    time.sleep(1.5)
	    print(f"{KIRMIZI}Lütfen tekrar deneyin{RESET}")
	    time.sleep(1.5)
	    os.system("clear")
																		
