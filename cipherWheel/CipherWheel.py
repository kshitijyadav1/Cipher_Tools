import sys

class CipherWheel:
	key = 0
	e_list = list()
	d_list = list()
	map = dict()
	r_map = dict()
	def __init__(self):
		''' constructor '''
		print("*"*50)
		self.welcome_msg()
		print("*"*50)
		self.key = self.key_formulator(self.ask_key())
		print("Now the default Key size: ", self.key)
		self.sync_flat()
		#self.inspector()
		
	def welcome_msg(self):
		print("Cipher Wheel encryption.")
		
	def ask_key(self):
		key = 0
		try:
			key = int(input("Enter key size: "))
		except:
			print("Oops! ", sys.exc_info()[0], " occured.")
		return key
		
	def fill_e_list(self):
		j = 65 # 'A'
		for i in range(0, 26):
			self.e_list.append(chr(j))
			j += 1
			
	def fill_d_list(self):
		self.fill_e_list()
		k = self.key
		for i in range(k, 0, -1):
			self.d_list.append((self.e_list[len(self.e_list) - i]))
		for i in range(0, (len(self.e_list) - k)):
			self.d_list.append(self.e_list[i])
		
			
	def show_e_list(self):
		print("______________ encode list _____________")
		for i in range(0, len(self.e_list)):
			print(i, " : ", self.e_list[i])
		
	def show_d_list(self):
		print("______________ decode list _____________")
		for i in range(0, len(self.d_list)):
			print(i, " : ", self.d_list[i])
			
	
	def key_formulator(self, key):
		if key >= 0 and key <= 25:
			pass
		elif key > 26:
			key = key % 26
		return key
			
	def fill_encode_mapping(self):
		for i in range(0, len(self.d_list)):
			self.map.setdefault(self.d_list[i], self.e_list[i])
			# ================   outer rings,    inner rings =====================
		self.map.setdefault(' ', ' ')
	
	
	def show_map(self):
		print("__________ Encode Mapping ____________")
		print(self.map)
			
	def fill_decode_mapping(self):
		for i in range(0, len(self.d_list)):
			self.r_map.setdefault(self.e_list[i], self.d_list[i])
			# ================   outer rings,    inner rings =====================
		self.r_map.setdefault(' ', ' ')
	
	
	def show_r_map(self):
		print("__________ Decode Mapping ____________")
		print(self.r_map)
	
	def sync_flat(self):
		self.fill_d_list()
		self.fill_encode_mapping()
		self.fill_decode_mapping()
	
	def inspector(self):
		self.show_e_list()
		self.show_d_list()
		self.show_map()
		self.show_r_map()
		
	def encrypt(self):
		msg = input("Enter messaage: ")
		for i in msg:
			print(i.upper()," ",end='')
		print("")
		print(":  "*len(msg))
		for i in msg:
			if i.isdigit():
				print(i," ",end='')
			else:
				print(self.map[i.upper()]," ",end='')
		print()
			
	def decrypt(self):
		msg = input("Enter messaage: ")
		for i in msg:
			print(i.upper()," ",end='')
		print("")
		print(":  "*len(msg))
		for i in msg:
			if i.isdigit():
				print(i," ",end='')
			else:
				print(self.r_map[i.upper()]," ",end='')
		print()
	
	def set_key(self):
		self.key = self.key_formulator(self.ask_key())
		
	def clearAll(self):
		self.key = 0
		self.e_list.clear()
		self.d_list.clear()
		self.map.clear()
		self.r_map.clear()