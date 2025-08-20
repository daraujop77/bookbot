from stats import count_words

def get_book_text(filepath):
	with open(filepath) as f:
		file_content = f.read()
	return file_content


def main():
	path = "/home/daraujopaez/github/bookbot/books/frankenstein.txt"
	book_text =  get_book_text(path)
	print(f"{count_words(book_text)} words found in the document"  )


main()
