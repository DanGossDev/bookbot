def wordcount(contents):
    return len(contents.split())

def charcount(contents):
    countlib_dict = {}
    characters = [char for char in contents]
    for character in characters:
        if character not in countlib_dict:
            countlib_dict[character.lower()] = 0
        countlib_dict[character.lower()] = countlib_dict[character] + 1
    return countlib_dict