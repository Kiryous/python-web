class Library:
	def __init__(self, string):
		self.books = dict()
		self.titles = []

		for pair in self.get_pairs(string.split(" ")):
			title, count = pair
			self.insert_book(title, int(count))
		
	def __del__(self):
		del self.books
	
	def get_pairs(self, l):
		return [l[i:i+2] for i in range(0, len(l), 2)]
	
	def insert_book(self, title, count):
		self.books[title] = count
		self.titles = sorted(self.books)
	
	def get_book_str(self, title):
		return "{} {}".format(title, self.get_book_count(title))

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

import hashlib
class LibraryHash:
	def __init__(self, lib, alg):
		self.lib = lib
		self.alg = alg
	
	def __del__(self):
		del self.lib
	
	def hash_books(self):
		return [getattr(hashlib, self.alg)(book.encode('utf-8')).hexdigest() 
			for book in self.lib.titles]
	
books_str = input()
alg = input()
lib = Library(books_str)
hash_lib = LibraryHash(lib, alg)

[print(lib.get_book_str(book)) for book in lib.titles]
print(" ".join([
	"{alg} {hash}".format(
		alg=hash_lib.alg,
		hash=bh
	) for bh in hash_lib.hash_books()
]))
