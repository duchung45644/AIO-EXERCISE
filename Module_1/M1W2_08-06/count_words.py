# Exercise: 3
# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    words_dict = {}

    words = text.lower().split()

    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return words_dict


if __name__ == '__main__':
    file_path = 'Module_1\\M1W2_08-06\\P1_data.txt'
    print(count_words(file_path))
