from random import randint

def random_ban_character(characters:list[str], nomber_of_banned: int) -> list[str]:
    """
    description: this is a function that take a list of characters and a number of ban characters and return a list of the banned characters.
    input : list of str + int
    output : list of str
    """
    banned_characters = []
    copy_characters = characters.copy()
    for i in range(nomber_of_banned):
        index = randint(0, len(copy_characters) - 1)
        banned_characters.append(copy_characters[index])
        copy_characters.pop(index)
    return banned_characters