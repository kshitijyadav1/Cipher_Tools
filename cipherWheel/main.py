from CipherWheel import CipherWheel

import sysdef main():
	''' main function '''
	e = CipherWheel() # initiate class constructor
	try:
		option = ask_option()
		while option != 6:
			if option == 1:
				e.clearAll()
				e.set_key()
				e.sync_flat()
			elif option == 2:
				e.encrypt()
			elif option == 3:
				e.decrypt()
			elif option == 4:
				e.show_map()
			elif option == 5:
				e.show_r_map()
			else:
				print("Good bye! XX")
				sys.exit()
			option = ask_option()
	except:
		print("Oops ! ", sys.exc_info()[0], " occured.")

def ask_option():
	''' it'll option to user, which is drastically appropriate to them. '''
	print("Enter number, according to the following choice: ")
	print("1 >> Set key")
	print("2 >> Encrypt message")
	print("3 >> Decrypt message")
	print("4 >> Show outer rings")
	print("5 >> Show inner rings")
	print("6 >> Exit")
	option = int(input("Enter number : "))
	return option
if __name__ == "__main__":
	main()
	