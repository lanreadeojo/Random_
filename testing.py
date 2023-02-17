#import unittest

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if not self.stack:
            raise IndexError("Cannot pop from empty stack")
        return self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        return True


# Stack Tester
'''
class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(100)
        self.assertFalse(self.stack.is_empty())

    def test_peak(self):
        self.stack.push('test')
        self.assertEqual(self.stack.peak(), 'test')

    def test_pop(self):
        self.stack.push(10.1)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_pop_value(self):
        self.stack.push('test_value')
        value = self.stack.pop()
        self.assertEqual(value,'test_value')

    def test_empty_pop(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

tests = StackTests()
'''

#buggy
class Hangman():
    def __init__(self):
        self.word = "aaat"
        self.wrong_guesses = 0
        self.stages = ["", "_______   ", "|  |  ", "|  O ","|  /|\   ", "|  /\    ", "|    "]
        self.letters_left = list(self.word)
        self.score_board = ['_'] * len(self.word)
        self.win = False
        print('Welcome to Hangman')

    def hangman(self):
        while self.wrong_guesses < len(self.stages) - 1:
            print(' \n ')
            guess = input("Guess a letter")
            if guess in self.letters_left:
                the_index = self.letters_left.index(guess)
                value = self.letters_left[the_index]
                self.score_board[the_index] = value
                self.letters_left[the_index] = '0'
            else:
                self.wrong_guesses += 1
                print((' '.join(self.score_board)))
                print('\n'.join(self.stages[0: self.wrong_guesses + 1]))
                if '_' not in self.score_board:
                    print('You win! The word was:')
                    print(' '.join(self.score_board))
                    self.win = True
                    break
        if not self.win:
            print('\n'.join(self.stages[0: self.wrong_guesses]))
            print('You lose! The words was {}'.format(self.word))


#class HangmanTest(unittest.TestCase):

        #def setUp(self):
         #self.hangman = Hangman()

        #def tearDown(self):
            #del self.hangman
'''
HangmanTest plan 
Test guess input is a string
Test win when word is correct
test wrong word count is =< word length
Test loss when word is incorrect and displays the 
test letters left is decreasing as you get closer to the word
check that word length is not greater than stages

'''



Hangman().hangman()
