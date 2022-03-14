import string

def load_words(file_name):
    with open(file_name) as word_file:
        word_list = list(word_file.read().split())
    return word_list


def get_letter_count_hash():
    alphabet_list = string.ascii_lowercase
    frequency_hash = {}
    for letter in alphabet_list:
        frequency_hash.update({letter: 0})
    return frequency_hash

def get_letter_frequency_hash(word_list):
    frequency_hash = get_letter_count_hash()
    for word in word_list:
        for letter in word:
            frequency_hash[letter] += 1
    return frequency_hash

def get_position_frequency_hash(word_list):
    position_frequency_hash_list = []
    for i in range(0, 5):
        position_frequency_hash_list.append(get_letter_count_hash())
    for word in word_list:
        position = 0
        for letter in word:
            position_frequency_hash_list[position][letter] += 1
            position += 1
    return position_frequency_hash_list


if __name__ == "__main__":
    solution_word_list = load_words('wordle_solution_words.txt')
    possible_solutions = solution_word_list.copy()
    #print(get_letter_frequency_hash(solution_word_list))
    print(get_position_frequency_hash(possible_solutions)[0])