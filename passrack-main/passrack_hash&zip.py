import hashlib
import sys
#import pyzipper
from zip import zip_k
import os

class colors:
    rGREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'
    lightblue = "\033[0;34m"

banner_2 = colors.RED + r"""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░██""" 	+colors.RED+"""██░▄█░░░░▒▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
▒░░░░░░░░████████████████████████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
████████████████████████████████████████████""" + colors.STOP
    

def banner():
    print (banner_2 + "\n")
    
    print("""    
    ██████╗░░█████╗░░██████╗░██████╗"""+colors.RED+"""  ██████╗░░█████╗░░█████╗░██╗░░██╗"""+colors.STOP+"""
    ██╔══██╗██╔══██╗██╔════╝██╔════╝"""+colors.RED+"""  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝"""+colors.STOP+"""
    ██████╔╝███████║╚█████╗░╚█████╗░"""+colors.RED+"""  ██████╔╝███████║██║░░╚═╝█████═╝░"""+colors.STOP+"""
    ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗"""+colors.RED+"""  ██╔══██╗██╔══██║██║░░██╗██╔═██╗░"""+colors.STOP+"""
    ██║░░░░░██║░░██║██████╔╝██████╔╝"""+colors.RED+"""  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗"""+colors.STOP+"""
    ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░"""+colors.RED+"""  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝""" + colors.STOP)
    

    print()

def zipcrack(filename, passlist):
    count = len(list(open(passlist, "rb")))
    print(colors.BLUE + "Total Passwords in File: " + colors.STOP, count)
    with open(passlist, "r") as words:
        for word in words:
            word = word.strip('\n')
            try:
                with pyzipper.AESZipFile('yourdocument.zip', 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
                    extracted_zip.extractall(pwd=str.encode(password))
            except:
                continue
            else:
                print(colors.GREEN + "[+] Password: " + colors.STOP, word.decode().strip())
                break
    print(colors.RED + "[!] Password Not found in the passlist, try with a different pass file." + colors.STOP)
    menu()

def md5 (choice, inp, passlist):
    m = hashlib.md5()
    if choice == 0:
        m.update(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
            password = line.strip('\n')
            m.update(password.encode("utf-8"))
            out=m.hexdigest()
            if out == inp:
                print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                print ("-"*30)
                c = 0
                menu()
            else: 
                c=c+1
                password = " "
        if c > 0:
            unable()
            menu()

def sha1 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha1(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha1(password.encode("utf-8"))
                out=m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else:
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha224 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha224(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                m = hashlib.sha224(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha256 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha256(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha256(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha384 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha384(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc(inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha384(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha512 (choice, inp, passlist):
        if choice == 0:
            m = hashlib.sha512(inp.encode("utf-8"))
            output = m.hexdigest()
            print_enc(inp, output)
            menu()
        if choice == 1:
            cracking()
            c=0
            passfile = open(passlist)
            for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha512(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()
            
def print_enc (inp, output):
    print ()
    print (colors.BOLD+"Hashing String..."+colors.STOP)
    print (colors.GREEN+inp + " : " + output+colors.STOP)
    print ()

def cracking():
    print (colors.BOLD+"Cracking String...\n"+colors.STOP+"-"*30)

def unable():
    print (colors.RED+"Unable to Find Password...\n"+colors.STOP+"-"*30)

def menu():
    banner()
    print ()
    print ("-"*70)
    print (colors.BOLD+"1.md5 \n2.sha1 \n3.sha224 \n4.sha256 \n5.sha384 \n6.sha512 \n7.ZIP File\n99.exit \n"+colors.STOP)
    value = int(input(">>> "))
    if value == 99:
        print (colors.RED+"QUITTING!!"+colors.STOP)
        sys.exit()

    if value >= 1 and value <= 6:
        choice = int(input("(0) for Hashing And (1) for Cracking : "))
        inp = str(input("String : "))
        
        if choice == 0:
            passlist = ''
        if choice == 1:
            passlist = input("PASSWORD FILE>>>")
    if value == 1:
        md5(choice, inp, passlist)
    if value == 2:
        sha1(choice, inp, passlist)
    if value == 3:
        sha224(choice, inp, passlist)
    if value == 4:
        sha256(choice, inp, passlist)
    if value == 5:
        sha384(choice, inp, passlist)
    if value == 6:
        sha512(choice, inp, passlist)
    if value == 7:
        zip_k()
        inpu = input('\x1b[6;30;42m'+"Press Enter to Continue..." + colors.STOP)
        menu()
os.system('clear')
menu()
