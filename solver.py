

# For importing the word lists from text files.
def get_list_from_file(file_name):
    return_list = []
    with open(file_name) as file:
        for line in file:
            return_list.append(line.strip())
    return return_list


# All of the logic for modifying the lists:
def remove_words_with_letter(word_list, letter):
    # use this when you have a grey score on a letter
    new_word_list = word_list.copy()
    for word in word_list:
        if letter in word:
            new_word_list.remove(word)
    return new_word_list

def remove_words_with_letter_in_position(word_list, letter, letter_index):
    # use this when you have a yellow score on a letter
    new_word_list = word_list.copy()
    for word in word_list:
        if word[letter_index] == letter:
            new_word_list.remove(word)
    return new_word_list

def remove_words_without_letter(word_list, letter):
    # use this when you have a yellow or green score on a letter
    new_word_list = word_list.copy()
    for word in word_list:
        if letter not in word:
            new_word_list.remove(word)
    return new_word_list

def remove_words_without_letter_in_position(word_list, letter, letter_index):
    # use this when you have a yellow score on a letter
    # use this when you have a green score as well(???)
    new_word_list = word_list.copy()
    for word in word_list:
        if word[letter_index] != letter:
            new_word_list.remove(word)
    return new_word_list


# interface for the list modifying logic
def get_possible_solution_count(word_list):
    return len(word_list)

def judge_word(solution_list, guess_list):
    print("")
    print("  --- --- ---  ")
    guess_word = input("What word did you guess?")
    position = 0
    for letter in guess_word:
        letter_score = input(f"What did '{letter}' score? (grey, green, yellow)")
        if letter_score == "grey":
            solution_list = remove_words_with_letter(solution_list, letter)
        elif letter_score == "green":
            solution_list = remove_words_without_letter_in_position(solution_list, letter, position)
        elif letter_score == "yellow":
            solution_list = remove_words_without_letter(solution_list, letter)
            solution_list = remove_words_with_letter_in_position(solution_list, letter, position)
        position += 1
    return (solution_list, guess_list)

def wordler_interface(solution_list, guess_list):
    while True:
        possible_solutions_count =  get_possible_solution_count(solution_list)
        print(f"There are {possible_solutions_count} possible solutions.")
        if possible_solutions_count <= 10:
            print("There are 10 or less solutions remaining:")
            print(solution_list)
        if get_possible_solution_count(solution_list) == 1:
            break
        solution_list, guess_list = judge_word(solution_list, guess_list)
    print(f"The answer is {solution_list[0]}")


# Note:
# need to also prune the guess list after getting information
# currently no handling for multiple letters in a word.


if __name__ == "__main__":
    solution_words = get_list_from_file('answers.txt')
    guess_words = get_list_from_file('guesses.txt')

    wordler_interface(solution_words, guess_words)