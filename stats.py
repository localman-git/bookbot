def count_book_words(book_text):
    return len(book_text.split())

def count_letter_appearances(book_text):
    count = {}
    for letter in book_text.lower():
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

def sort_on(list):
    return list['num']

def sorted_letter_dictionaries(dict):
    list = []
    for k in dict:
        if k.isalpha():
            list.append({'letter': k, 'num': dict[k]})
    list.sort(reverse=True, key=sort_on)
    return list