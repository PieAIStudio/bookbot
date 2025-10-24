def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    dic_list = []
    for k in char_counts:
        dic_list.append({'name': k, 'num': char_counts[k]})
    def sort_on(items):
        return items["num"]
    dic_list.sort(reverse=True, key=sort_on)
    for item in dic_list:
        if item['name'].isalpha():
            print(f"{item['name']}: {item['num']}")
