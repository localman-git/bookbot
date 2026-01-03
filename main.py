from stats import count_book_words, count_letter_appearances, sorted_letter_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():

    book_filepath = './books/frankenstein.txt'
    book_text = get_book_text(book_filepath)

    character_count = count_letter_appearances(book_text)
    sorted_character_count = sorted_letter_dictionaries(character_count)
    
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {count_book_words(book_text)} total words')
    print('--------- Character Count -------')
    for dict in sorted_character_count:
        print(f'{dict['letter']}: {dict['num']}')
    print('============= END ===============')

main()