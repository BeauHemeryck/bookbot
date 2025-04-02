from stats import get_amount_of_word, get_book_text, get_amount_of_char, sort_dictionary
def main():
    frank_path = "./books/frankenstein.txt"
    frank = get_book_text(frank_path)
    num_words = get_amount_of_word(frank)
    char_count = sort_dictionary(get_amount_of_char(get_book_text("./books/frankenstein.txt")))
    print(f"============ BOOKBOT ============\nAnalyzing book found at {frank_path[2:]}\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for char in char_count:
        if char.isalpha():
            print(f"{char}: {char_count[char]}")

main()