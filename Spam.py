#!/bin/python


import os,sys,time

def bersih():
    os.system("clear")

def menu():
    bersih()
    print "========================================"
    print "    Author       :   MANXPLOIT          "
    print "   Whatsapp      :  +1668827887         "
    print "   facebok       : Orochimaru Sama      "
    print "========================================"
    print "[1] intall DarkFb "
    print "[2] Install Metasploit "
    print "[3] Keluar/Exit "
    pil = raw_input("Pilih Sesuai Nomor : ")
    if pil =="1":
        os.system("pkg update && pkg upgrade -y")
        os.system("pkg install git -y")
        os.system("pkg install python2")
        os.system("git clone https://github.com/MAN-ID/DarkFb")
    elif pil =="2":
        os.system("pkg update && pkg upgrade -y")
        os.system("pkg install git -y")
        os.system("pkg install python2")
        os.system("git clone https://github.com/MAN-ID/Metasploit")
    elif pil =="3":
        sys.exit()
menu()