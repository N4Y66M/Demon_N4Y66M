import os, platform,time
os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://www.facebook.com/groups/660205018582939")
#os.system("clear")
#print("\t 30 April ko All Approvels Remove Krdea jaingy")
#print("\t Users Ko Again Buy Krna pady ga ")
#print("\t Shukriya.....")
#time.sleep(3)
#print("updating again please wait we have some errors")
#exit()
try:
    import requests
except(ImportError):
    os.system("pip install requests")
try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")

N4Y66M=platform.architecture()[0]
try:
    if N4Y66M=="32bit":
        
    elif N4Y66M=="64bit":
        __import__("N4Y66M").mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if N4Y66M == "32bit":
        import pro32
        pro32.mysecurity()
    elif N4Y66M == "64bit":
        import N4Y66M
        N4Y66M.mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
