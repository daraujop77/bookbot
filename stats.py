
def sort_key(e):
	return e['num']

def sort_dict(dict_new):
	new_list = []
	sorted_dict = {}
	for char, num in dict_new.items():
		if char.isalpha():
			new_list.append({"char" : char, "num": num})
	
	new_list.sort(key=sort_key, reverse=True)
#	sorted_dict = dict(new_list)
#	print(type(sorted_dict))
	return new_list		
	
def count_words(books_content):
	word_list = []
	word_list = books_content.split()
	return len(word_list)

def char_rep(book_content):
	dict = {}
	book_content = book_content.lower()
	for char in book_content:
		if char in dict:
			dict[char] += 1
		else:
			dict[char] = 1
	
	return dict
