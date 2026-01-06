def count_words(text):
    total = len(text.split())
    return total 

def count_characters(text):
    characters = {}
    for i in text:
        i = i.lower()
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

def sort_on(dictionary):
    return dictionary["num"]

def convert_sort(characters):
    dict_list = []
    for i, j in characters.items():
        dict_list.append({"char": i, "num": j})
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list

    
