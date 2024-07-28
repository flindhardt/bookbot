def count_words(content):
    words = content.split()
    count = 0
    for word in words:
        count += 1
    print(count)

def main():
    book_dir = "./books/"
    with open(f"{book_dir}frankenstein.txt") as f:
        book_content = f.read()
        count_words(book_content)


main()