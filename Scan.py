import socket, os, time, threading, colorama
import scapy.all as scapy
from colorama import Fore
from datetime import datetime
from socket import*

print_lock = threading.Lock()


def scan():
	print(Fore.MAGENTA +"                      _____  _____          _   _  \n"
		  			   +" ******************* / ____|/ ____|   /\   | \ | | ******************\n"
		  			   +" ****************** | (___ | |       /  \  |  \| | ******************\n"
		  			   +" ******************* \___ \| |      / /\ \ | . ` | ******************\n"
		  			   +" ******************* ____) | |____ / ____ \| |\  | ******************\n"
		  			   +" ****************** |_____/ \_____/_/    \_\_| \_| ******************\n" + Fore.RESET + Fore.GREEN)


	scn = input(		 " Article 323-1 : Le fait d'accéder ou de se maintenir, frauduleusement,\n"
						 " dans tout ou une partie d'un système de traitement automatisé de données\n"
						 " est puni de deux ans d'emprisonnement et de 60 000 € d'amende\n\n"

						 " 1- Balayage De Ping (Very-Low)\n"
						 " 2- Scanner De Port (Low)\n"
						 " 3- Scanner TCP Pour Les Systèmes Windows (Fast)\n"
						 " 4- Scanner De Port filetés /!/Beta not stable/!/ (Fast)\n"
						 " 5- Écouter le réseau (1x)\n"
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
	nbre = input(" combien de fois >: ") 
	filtre = 'host '+ ip_target
	snf = scapy.sniff(count=int(nbre), filter=filtre, prn=lambda x:x.show())
	scapy.load_layer('tls')
	try:
		TLS(snf)
	except:
		print(Fore.RED + "is not encoding in tls" + Fore.GREEN)
