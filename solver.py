import string


# For importing the word lists from text files.
def get_list_from_file(file_name):
    return_list = []
    with open(file_name) as file:
        for line in file:
            return_list.append(line.strip())
    return return_list


class WordleList:
    def __init__(self, solution_word_list, all_words_list):
        self.word_list = solution_word_list
        self.all_words_list = all_words_list
        self.letter_frequency_dict = {}
        self.correct_letters = []

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
        # use this when you have a green score on a letter
        new_word_list = self.word_list.copy()
        for word in self.word_list:
            if word[letter_index] != letter:
                new_word_list.remove(word)
        self.word_list = new_word_list

    def remove_words_with_two_letter(self, letter):
        # use this when you have a grey score on the second of the same letter
        new_word_list = self.word_list.copy()
        for word in self.word_list:
            if word.count(letter) >= 2:
                new_word_list.remove(word)
        self.word_list = new_word_list

    def count(self):
        return len(self.word_list)

    def initialize_frequency_dict(self):
        alphabet_dict = {}
        for letter in string.ascii_lowercase:
            alphabet_dict.update({letter: 0})
        self.letter_frequency_dict = alphabet_dict

    def analyze(self):
        self.initialize_frequency_dict()
        for word in self.word_list:
            for letter in word:
                current_value = self.letter_frequency_dict[letter]
                self.letter_frequency_dict.update({letter: current_value + 1})
    
    def get_most_common_letters(self):
        return self.letter_frequency_dict.copy()

    def input_letter_details(self, letter, position, grade):
        if grade == 'grey':
            self.remove_words_with_letter(letter)
        elif grade == 'green':
            self.remove_words_without_letter_in_position(letter, position)
            if letter not in self.correct_letters:
                self.correct_letters.append(letter)
        elif grade == 'yellow':
            self.remove_words_without_letter(letter)
            self.remove_words_with_letter_in_position(letter, position)
            if letter not in self.correct_letters:
                self.correct_letters.append(letter)

    def input(self, graded_word_details):
        letters, grades = graded_word_details
        graded_letters = []
        while len(graded_letters) < len(letters):
            # grade greens, then yellows, then greys
            if 'green' in grades:
                index = grades.index('green')
                letter = letters[index]
                self.input_letter_details(letter, index, 'green')
                graded_letters.append(letter)
                grades[index] = ''
            elif 'yellow' in grades:
                index = grades.index('yellow')
                letter = letters[index]
                self.input_letter_details(letter, index, 'yellow')
                graded_letters.append(letter)
                grades[index] = ''
            elif 'grey' in grades:
                index = grades.index('grey')
                letter = letters[index]
                if letter in graded_letters:
                    self.remove_words_with_two_letter(letter)
                else:
                    self.input_letter_details(letter, index, 'grey')
                graded_letters.append(letter)
                grades[index] = ''

    def get_exclusion_guess_recommendation(self):
        word_score_dict = {}
        for word in self.all_words_list:
            word_score = 0
            repeated_letters = []
            for letter in word:
                if letter not in repeated_letters and letter not in self.correct_letters:
                    word_score += self.letter_frequency_dict[letter]
                repeated_letters.append(letter)
            word_score_dict.update({word_score: word})
        values_list = sorted(word_score_dict.keys())
        highest_score = values_list.pop()
        best_word = word_score_dict[highest_score]
        return best_word

    def get_answer_guess_recommendation(self):
        word_score_dict = {}
        for word in self.word_list:
            word_score = 0
            repeated_letters = []
            for letter in word:
                if letter not in repeated_letters:
                    word_score += self.letter_frequency_dict[letter]
                repeated_letters.append(letter)
            word_score_dict.update({word_score: word})
        values_list = sorted(word_score_dict.keys())
        highest_score = values_list.pop()
        best_word = word_score_dict[highest_score]
        return best_word


class WordleHelper:
    def __init__(self, wordle_list):
        self.wordle_list = wordle_list

    def input_score_for_word(self, guess_word):
        letters = []
        grades = []
        valid_scores = ['grey', 'yellow', 'green']
        for letter in guess_word:
            grade = input(f"What did '{letter}' score? (grey, green, yellow)")
            while grade not in valid_scores:
                print("invalid score")
                grade = input(f"What did '{letter}' score? (grey, green, yellow)")
            letters.append(letter)
            grades.append(grade)
        graded_word_details = (letters, grades)
        self.wordle_list.input(graded_word_details)
    
    def wordler_interface(self):
        while True:
            self.wordle_list.analyze()
            possible_solutions_count =  self.wordle_list.count()
            if possible_solutions_count == 1:
                break
            print(f"There are {possible_solutions_count} possible solutions.")
            print(f"Exclusion Guess: {self.wordle_list.get_exclusion_guess_recommendation()}.")
            print(f"Answer Guess: {self.wordle_list.get_answer_guess_recommendation()}.")
            guess_word = input("What word did you guess?")
            self.input_score_for_word(guess_word)
        print(f"The answer is {self.wordle_list.word_list[0]}")


if __name__ == "__main__":
    solution_words = get_list_from_file('answers.txt')
    guess_words = get_list_from_file('guesses.txt')
    whole_list = solution_words.copy() + guess_words.copy()

    solution_list = WordleList(solution_words, whole_list)

    helper = WordleHelper(solution_list)
    helper.wordler_interface()