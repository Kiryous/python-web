class Library:
	def __init__(self, string):
		self.books = dict()

		for pair in self.get_pairs(string.split(" ")):
			title, count = pair
			self.insert_book(title, int(count))
		
	def __del__(self):
		del self.books
	
	def get_pairs(self, l):
		return [l[i:i+2] for i in range(0, len(l), 2)]
	
	def insert_book(self, title, count):
		self.books[title] = count

	def get_book_count(self, title):
		if title not in self.books:
			return
		return self.books[title]
	
	def inc_book(self, title):
		self.books[title] += 1
		return self.books[title]
		
	def dec_book(self, title):
		self.books[title] -= 1
		return self.books[title]
	
string = input()
lib = Library(string)

print(" ".join([
	"{title} {count} {dec} {inc}".format(
		title=book, 
		count=lib.get_book_count(book),
		dec=lib.dec_book(book),
		inc=lib.inc_book(book)
		)
	for book in lib.books
]))