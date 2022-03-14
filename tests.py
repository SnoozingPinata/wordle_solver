import wordle_solver

def test_load_words():
    guess_word_list = wordle_solver.load_words('wordle_guess_words.txt')
    solutions_word_list = wordle_solver.load_words('wordle_solution_words.txt')
    if len(guess_word_list) == 10657 and len(solutions_word_list) == 2315:
        print("SUCCESS: Test load_words passed.")

def test_get_letter_frequency_hash():
    solutions_word_list = wordle_solver.load_words('wordle_solution_words.txt')
    correct_results = {'a': 979, 'b': 281, 'c': 477, 'd': 393, 'e': 1233, 'f': 230, 'g': 311, 'h': 389, 'i': 671, 'j': 27, 'k': 210, 'l': 719, 'm': 316, 'n': 575, 'o': 754, 'p': 367, 'q': 29, 'r': 899, 's': 669, 't': 729, 'u': 467, 'v': 153, 'w': 195, 'x': 37, 'y': 425, 'z': 40}
    if wordle_solver.get_letter_frequency_hash(solutions_word_list) == correct_results:
        print("SUCCESS: Test get_letter_frequency_hash passed.")

if __name__ == "__main__":
    test_load_words()
    test_get_letter_frequency_hash()