BOOK_DIR = "./books/"
BOOK_FILE = "frankenstein.txt"
REPORT_START = f"----------------- Begin Report of {BOOK_DIR}{BOOK_FILE} -----------------"
REPORT_END = f"----------------- End Report of {BOOK_DIR}{BOOK_FILE} -----------------"

def main():
    with open(f"{BOOK_DIR}{BOOK_FILE}") as f:
        book_content = f.read()
    dict_char = dict_to_list_of_dicts(count_chars(book_content))
    dict_char.sort(reverse=True,key=sort_chars)
    print()
    print(f"{REPORT_START}")
    print()
    print(f"{count_words(book_content)} words were found")
    print()
    for char in dict_char:
        print(f"{char['char']} kommt {char['amount']} mal vor")
    print()
    print(REPORT_END)



def sort_chars(dict):
    return dict["amount"]

def dict_to_list_of_dicts(dict):
    list_of_dicts = [{'char': key, 'amount': value} for key, value in dict.items()]
    return list_of_dicts

def count_words(content):
    words = content.split()
    return len(words)

def count_chars(content):
    lower_content = content.lower()
    char_dict = {}
    for char in lower_content:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
    

main()