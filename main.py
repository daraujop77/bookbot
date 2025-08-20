from stats import count_words
from stats import char_rep
from stats import sort_dict

def get_book_text(filepath):
	with open(filepath) as f:
		file_content = f.read()
	return file_content


def main():
	import pprint
	path = "/home/daraujopaez/github/bookbot/books/frankenstein.txt"
	book_text =  get_book_text(path)
	print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
	print(f"Found {count_words(book_text)} total words")
	print("--------- Character Count -------")
	chars = char_rep(book_text)
	sorted_chars = sort_dict(chars)
	for char in sorted_chars:
		print(f"{char['char']}: {char['num']}")		
	print("============= END ===============")

main()
