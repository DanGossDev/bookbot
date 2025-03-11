def wordcount(contents):
    return len(contents.split())

def charcount(contents):
    countlib_dict = {}
    characters = [char for char in contents]
    for character in characters:
        if character.lower() not in countlib_dict:
            countlib_dict[character.lower()] = 0
        count = countlib_dict[character.lower()] + 1
        countlib_dict[character.lower()] = count
    return countlib_dict


def sort_dict(contents):
    char_list = []
    for char, count in contents.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list