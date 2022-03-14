

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


class WordleHelper:
    def __init__(self, wordle_list):
        self.wordle_list = wordle_list

    def judge_word(self):
        print("\n" + "  --- --- ---  " + "\n")
        guess_word = input("What word did you guess?")
        position = 0
        for letter in guess_word:
            letter_score = input(f"What did '{letter}' score? (grey, green, yellow)")
            if letter_score == "grey":
                self.wordle_list.remove_words_with_letter(letter)
            elif letter_score == "green":
                self.wordle_list.remove_words_without_letter_in_position(letter, position)
            elif letter_score == "yellow":
                self.wordle_list.remove_words_without_letter(letter)
                self.wordle_list.remove_words_with_letter_in_position(letter, position)
            position += 1

    def wordler_interface(self):
        while True:
            possible_solutions_count =  self.wordle_list.count()
            if possible_solutions_count == 1:
                break
            elif possible_solutions_count <= 10:
                print("There are 10 or less solutions remaining:")
                print(self.wordle_list.word_list)
            print(f"There are {possible_solutions_count} possible solutions.")
            self.judge_word()
        print(f"The answer is {self.wordle_list.word_list[0]}")


# Note:
# need to also prune the guess list after getting information
# currently no handling for multiple letters in a word.


if __name__ == "__main__":
    solution_words = get_list_from_file('answers.txt')
    guess_words = get_list_from_file('guesses.txt')

    solution_list = WordleList(solution_words)
    guess_list = WordleList(guess_words)

    helper = WordleHelper(solution_list)
    helper.wordler_interface()