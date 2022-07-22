import mmh3
from bitarray import bitarray

class HashFilter(object):

	'''
	created by Maor shapochnikov 313238826
	'''

	def __init__(self, k,m):
		'''
		constractor
		:param k: number of Hash functions
		:param m: the size of the bit array
		'''

		self.array_size = m
		self.function_count = k
		self.bit_array = bitarray(self.array_size)
		self.bit_array.setall(0)

	def add_item(self, item):
		'''
		Add an item into the filter
		:param item: item to insert
		'''
		for i in range(self.function_count):
			digest = mmh3.hash(item, i) % self.array_size
			self.bit_array[digest] = True

	def check_item(self, item):
		'''
		Check for existence of an item in the filter
		:param item: checking if the item is inside the file
		:return: if exists True else False
		'''
		for i in range(self.function_count):
			digest = mmh3.hash(item, i) % self.array_size
			if self.bit_array[digest] == False:
				return False
		return True

def get_user_input():
	'''
	get's the user input (two numbers(integer))
	'''
	k,m=input("plese enter k and m values separated by white space").split()
	k=int(k)
	m=int(m)
	return k,m

def read_data_from_file(file_name):
	'''
	read's data from the given file.
	the data file needs to be separated by comma.
	:param file_name: the file name
	:return: list of data or none
	'''
	data=""
	with open(file_name, 'r') as file:
		data=file.read()
	if data != "":
		list=[item for item in data.split(",")]
		return list
	return None

def main():
	try:
		k, m = get_user_input()
		insert_items = read_data_from_file("insert_items.txt")
		search_items = read_data_from_file("search_items.txt")
		hash_filter = HashFilter(k, m)

		for item in insert_items:  # inserting the data into the HushFilter
			hash_filter.add_item(item)

		for item in search_items:  # checking if the item is inside the HushFilter
			res = hash_filter.check_item(item)
			if res:
				print("item: " + item + " exists")
			else:
				print("item: " + item + " do not exists")
	except :
		print('Error occurred')


if __name__ == "__main__":
	main()
