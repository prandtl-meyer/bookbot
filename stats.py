def count_words(text):
    # This function counts the number of words in a given text.
    words = text.split()
    return len(words)

def count_each_character(text):
    # This function counts the occurrences of each character in a given text.
    char_count = {}
    for char in text:
        char = char.lower()
        # Convert character to lowercase for case-insensitive counting
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dictionary(dictio):
    # This function takes a dictionary and returns a sorted list of dictionaries.
    list = []
    for item in dictio:
        list.append({"char": item, "num": dictio[item]})
    
    list.sort(reverse=True, key=lambda item: item["num"])
    return list

    

