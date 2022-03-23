import string

# For importing the word lists from text files.
def get_list_from_file(file_name):
    return_list = []
    with open(file_name) as file:
        for line in file:
            return_list.append(line.strip())
    return return_list


class WordleList:
    def __init__(self, word_list):
        self.word_list = word_list
        self.letter_frequency_list = []

    def remove_words_with_letter(self, letter):
        # use this when you have a grey score on a letter
        new_word_list = self.word_list.copy()
        for word in self.word_list:
            if letter in word:
                new_word_list.remove(word)
        self.word_list = new_word_list

    def remove_words_with_letter_in_position(self, letter, letter_index):
        # use this when you have a yellow score on a letter
        new_word_list = self.word_list.copy()
        for word in self.word_list:
            if word[letter_index] == letter:
                new_word_list.remove(word)
        self.word_list = new_word_list

    def remove_words_without_letter(self, letter):
        # use this when you have a yellow or green score on a letter
        new_word_list = self.word_list.copy()
        for word in self.word_list:
            if letter not in word:
                new_word_list.remove(word)
        self.word_list = new_word_list

    def remove_words_without_letter_in_position(self, letter, letter_index):
        # use this when you have a yellow score on a letter
        # use this when you have a green score as well(?)
        new_word_list = self.word_list.copy()
        for word in self.word_list:
            if word[letter_index] != letter:
                new_word_list.remove(word)
        self.word_list = new_word_list

    def count(self):
        return len(self.word_list)

    def _get_numeric_value_of_letter(self, letter):
        alphabet_list = string.ascii_lowercase
        return alphabet_list.index(letter)

    def _get_alphabetical_value_of_number(self, number):
        alphabet_list = string.ascii_lowercase
        return alphabet_list[number]

    def _get_blank_letter_count_list(self):
        blank_list = []
        for i in range(0, 26):
            blank_list.append(0)
        return blank_list

    def update_letter_frequency_list(self):
        letter_frequency_list = self._get_blank_letter_count_list()
        for word in self.word_list:
            for letter in word:
                index = self._get_numeric_value_of_letter(letter)
                letter_frequency_list[index] += 1
        self.letter_frequency_list = letter_frequency_list
    
    def get_most_common_letters(self):
        return self.letter_frequency_list


class WordleHelper:
    def __init__(self, wordle_list):
        self.wordle_list = wordle_list

    def input_score_for_word(self, guess_word):
        print("\n" + "  --- --- ---  " + "\n")
        position = 0
        for letter in guess_word:
            letter_score = input(f"What did '{letter}' score? (grey, green, yellow)")
            grey_score = letter_score == "grey"
            green_score = letter_score == "green"
            yellow_score = letter_score == "yellow"
            if grey_score:
                self.wordle_list.remove_words_with_letter(letter)
            elif green_score:
                self.wordle_list.remove_words_without_letter_in_position(letter, position)
            elif yellow_score:
                self.wordle_list.remove_words_without_letter(letter)
                self.wordle_list.remove_words_with_letter_in_position(letter, position)
            position += 1
    
    def print_list_analytics(self):
        print("")
        self.wordle_list.update_letter_frequency_list()
        print("Most common letters:")
        alphabet_list = string.ascii_lowercase
        letter_count_list = self.wordle_list.get_most_common_letters()
        for i in range(0, 26):
            current_letter = alphabet_list[i]
            letter_count_value = letter_count_list[i]
            if letter_count_value != 0:
                print(f"{current_letter} = {letter_count_value}")
        print("")

    def wordler_interface(self):
        while True:
            possible_solutions_count =  self.wordle_list.count()
            if possible_solutions_count == 1:
                break
            elif possible_solutions_count <= 20:
                print("There are 20 or less solutions remaining:")
                print(self.wordle_list.word_list)
            print(f"There are {possible_solutions_count} possible solutions.")
            self.print_list_analytics()
            guess_word = input("What word did you guess?")
            self.input_score_for_word(guess_word)
        print(f"The answer is {self.wordle_list.word_list[0]}")


# Note:
# need to also prune the guess list after getting information
# currently no handling for multiple letters in a word.
# first, third, and fifth positions seem to cancel more words out. 


if __name__ == "__main__":
    solution_words = get_list_from_file('answers.txt')
    #guess_words = get_list_from_file('guesses.txt')

    #whole_list = solution_words + guess_words

    solution_list = WordleList(solution_words)
    #solution_list = WordleList(whole_list)
    #guess_list = WordleList(guess_words)

    helper = WordleHelper(solution_list)
    helper.wordler_interface()