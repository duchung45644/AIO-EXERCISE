# # Exercise: 2

def count_chars(string):
    char_dict = {}

    for c in string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict


if __name__ == '__main__':
    string = 'Happiness'
    print(count_chars(string))

    string = 'smiles'
    print(count_chars(string))
