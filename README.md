# wordle_solver
A tool for solving the daily NY Times wordle!

Strategy Goals:
  (primary) Solve the puzzle correctly.
  (secondary) Solve the puzzle in as few tries as possible.

General Strategy:
  Determine the best starting word based on the dictionary of possible answers.
  Based on results, pick the best strategy for the next guess.
  Pick the best word for the given strategy.
  Repeat previous 2 steps.

word picking strategies:
  solution guess - choosing the most likely word to be the solution
  exclusion guess - a guess used to rule out as many possible solutions as possible
  mixed guess - a word chosen to test specific letters for a solution and other letters exclusionarily
  hit guess - a word chosen to try to find information (like a first or possibly second word choice)