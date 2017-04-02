class lib:
	
	def __init__(self):
		self.name = ''
		self.book = dict()
		
	def __del__(self):
		pass
	
	def insert_book(self, name, num):
		self.book[name] = num

	def get_num_book(self, name):
		return self.book[name]
	
	def inc_book(self, name):
		self.book[name] += 1
		return self.book[name]
		
	def dec_book(self, name):
		self.book[name] -= 1
		return self.book[name]
	
s = input()

books = s.split(' ')[0::2]
nums = s.split(' ')[1::2]

bks = lib()

s = ''

for book, num in zip(books, nums):
	bks.insert_book(book, int(num))
	if s != '':
		s += ' '
	s += book + ' ' + str(bks.get_num_book(book)) + ' ' + str(bks.dec_book(book)) + ' ' + str(bks.inc_book(book))

print(s)