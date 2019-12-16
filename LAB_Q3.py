'''
Python Version used: 3.7.4 
Authors: Dhanraj Vedanth Raghunathan, Kashish Singh
Note: Have the q3.textfsm file on the same folder as this python script!
'''

from netmiko import ConnectHandler
import textfsm
import os
import re

flag = 0
fsm_results = []
ip_addr = ''
mac_addr = ''

def check_ip():
	global ip_addr
	ip_addr = input("What is the IP Address?\n")
	ip_pat = (r"(\d+\.\d+\.\d+\.\d+)")
	ip_match = re.search(ip_pat,str(ip_addr))
	if not ip_match:
		if (ip_addr == ''):
			print("IP address not entered by the user\n")
		else:
			print("Invalid IP, Enter again:")
			check_ip()
	else:
		print("Accepted\n")

def check_mac():
	global mac_addr
	mac_addr = input("What is the Mac Address?\n")
	mac_pat = (r"([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])")
	mac_match = re.search(mac_pat,str(mac_addr))
	if not mac_match:
		if (mac_addr == ''):
			print("MAC address not entered by the user\n")
		else:
			print("Invalid MAC, Enter again:")
			check_mac()
	else:
		print("Accepted!\n")

def generator():
	global ip_addr,mac_addr, fsm_results
	# print("Trying to connect")
	net_connect = ConnectHandler(device_type='linux', host='152.46.19.75', username='draghun', password='Hourglass!5') 
	# print("connected!")
	output = net_connect.send_command('ifconfig')

	# print("ifconfig:\n" + output)

	template = open(os.path.join(os.getcwd(),"q3.textfsm"))
	re_table = textfsm.TextFSM(template)
	fsm_results = re_table.ParseText(output)
#	print(re_table.header)
	# print(fsm_results)
def flexible_match():
	global fsm_results
	for main_list in fsm_results:
		iface = main_list[1].split("  ")
		# print(iface)
		if (iface[0] == "Local"):
		 	iface[0] = "Local Loopback"
		 	main_list[2] = "N/A"

		if (str(type_detail).lower() == ''):
			pass
		else:
			if (str(type_detail).lower() in str(iface[0]).lower()):
				print("\nMatch found for the input 'Interface Type': ",str(type_detail),"\n")
				print("\nThis is the corresponding details:\n")
				print("Interface Name:",main_list[0],"\nInterface Type:",iface[0],
					"\nMAC Address:",main_list[2],"\nIPv4 address:",main_list[3],"\nIPv4 mask:",main_list[4]
					,"\nIPv6 address:",main_list[5],"\nIPv6 mask:",main_list[6])

		if (str(ip_addr) == ''):
			pass
		else:
			if(str(ip_addr) == str(main_list[3])):
				print("\nMatch found for the input 'IP Address': ",str(ip_addr),"\n")
				print("\nThis is the corresponding details:\n")
				print("Interface Name:",main_list[0],"\nInterface Type:",iface[0],
					"\nMAC Address:",main_list[2],"\nIPv4 address:",main_list[3],"\nIPv4 mask:",main_list[4]
					,"\nIPv6 address:",main_list[5],"\nIPv6 mask:",main_list[6])

		
		if (str(mac_addr) == ''):
			pass	
		else:	
			if(str(mac_addr) == str(main_list[2])):
				print("\nMatch found for input 'MAC Address': ",str(mac_addr),"\n")
				print("\nThis is the corresponding details:\n")
				print("Interface Name:",main_list[0],"\nInterface Type:",iface[0],
					"\nMAC Address:",main_list[2],"\nIPv4 address:",main_list[3],"\nIPv4 mask:",main_list[4]
					,"\nIPv6 address:",main_list[5],"\nIPv6 mask:",main_list[6])

def strict_match():
	global fsm_results
	for main_list in fsm_results:
		iface = main_list[1].split("  ")
		# print(iface)
		if (iface[0] == "Local"):
		 	iface[0] = "Local Loopback"
		 	main_list[2] = "N/A"

		if ((str(type_detail).lower() == '') and (str(ip_addr) == '') and (str(mac_addr) == '')):
			print("All inputs empty! \n Please provide inputs to find a match!")
			exit()
		else:
			if main_list[2] == "N/A":
				if ((str(type_detail).lower() in str(iface[0]).lower()) and (str(ip_addr) == str(main_list[3]))):
					print("\nMatch found for the input 'Interface Type': ",str(type_detail),"\n")
					print("\nThis is the corresponding details:\n")
					print("Interface Name:",main_list[0],"\nInterface Type:",iface[0],
						"\nMAC Address:",main_list[2],"\nIPv4 address:",main_list[3],"\nIPv4 mask:",main_list[4]
						,"\nIPv6 address:",main_list[5],"\nIPv6 mask:",main_list[6])
			else:

				if ((str(type_detail).lower() in str(iface[0]).lower()) and (str(ip_addr) == str(main_list[3])) and (str(mac_addr) == str(main_list[2]))):
					print("\nMatch found for the input 'Interface Type': ",str(type_detail),"\n")
					print("\nThis is the corresponding details:\n")
					print("Interface Name:",main_list[0],"\nInterface Type:",iface[0],
						"\nMAC Address:",main_list[2],"\nIPv4 address:",main_list[3],"\nIPv4 mask:",main_list[4]
						,"\nIPv6 address:",main_list[5],"\nIPv6 mask:",main_list[6])

def flag_collection():
	global flag
	flag = input("Please select from the two methods of search:\n1.Strict Matching.      2.Flexible Matching.\nOption(1 or 2):")
	if ((int(flag) == 1) or (int(flag) == 2)):
		print("Thanks!\n")
	else:
		print("Invalid input!, valid inputs are 1 or 2!\n")
		flag_collection()
		

flag_collection()
type_detail = input("What is the interface type?\n")
if (str(type_detail).lower() == ''):
		print("Type detail not entered by the user\n")
check_ip()
check_mac()
generator()
print(flag)
if(int(flag) == 2):
	print("You chose flexible matching\nMatches with respect to any single field would yeild a result\n")
	flexible_match()
elif(int(flag) == 1):
	print("You chose strict matching\nOutput can be seen only if all the three inputs match an interface detail\n")
	strict_match()


# print(fsm_results)

