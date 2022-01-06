import unittest
from sudoku import *

# For file to be discovered by python -m unittest discover;
# file name should be a legal Python identifier and should start with test
# Also function name should start with test

class SudokuTest(unittest.TestCase):

	def test_medium(self):
		sudoku = [
			[0,5,3, 4,0,0, 0,6,0],
			[0,0,0, 0,0,5, 1,7,0],
			[0,0,6, 9,0,0, 4,0,3],
			[5,0,0, 7,3,4, 0,0,0],
			[0,8,0, 0,0,0, 0,3,0],
			[0,0,0, 6,5,8, 0,0,2],
			[0,0,1, 0,0,3, 9,0,0],
			[0,2,9, 5,0,0, 0,0,0],
			[0,7,0, 0,0,1, 3,4,0]
			]
		execute_sudoku(sudoku)
		print_sudoku(sudoku)

	def test_medium_2(self):
		sudoku = [
			[0,0,8, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,2],
			[9,6,0, 3,7,0, 5,0,0],
			[6,5,9, 7,4,0, 0,2,1],
			[8,2,0, 0,9,5, 0,0,4],
			[0,0,1, 0,0,8, 7,0,0],
			[1,3,2, 4,6,7, 9,0,5],
			[4,0,0, 0,3,1, 0,0,0],
			[0,8,6, 0,0,9, 0,0,0]
			]
		execute_sudoku(sudoku)
		print_sudoku(sudoku)

	def test_hard(self):
		sudoku = [
			[0,0,2, 5,3,9, 8,1,6],
			[0,0,9, 8,0,0, 2,7,0],
			[6,1,0, 2,4,0, 0,0,0],
			[2,3,0, 7,0,0, 0,0,5],
			[9,7,0, 0,0,0, 0,0,1],
			[0,8,5, 0,0,0, 0,0,0],
			[0,9,0, 0,0,0, 0,6,0],
			[0,0,0, 0,6,0, 0,4,7],
			[5,6,4, 0,7,3, 1,2,0]
			]
		execute_sudoku(sudoku)
		print_sudoku(sudoku)

	def test_expert(self):
		print("expert")
		sudoku = [
			[0,4,9, 0,8,0, 7,0,0],
			[0,0,0, 0,0,0, 0,2,0],
			[0,0,0, 9,5,0, 8,0,0],
			[5,3,0, 0,9,0, 0,0,0],
			[0,0,8, 0,0,0, 0,0,7],
			[1,0,0, 3,0,2, 0,0,5],
			[0,0,4, 0,6,1, 0,0,0],
			[0,0,0, 0,0,0, 3,0,0],
			[0,0,0, 7,0,0, 0,0,0]
			]
		execute_sudoku(sudoku)
		print_sudoku(sudoku)

	def test_zero(self):
		sudoku = [
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0],
			[0,0,0, 0,0,0, 0,0,0]
			]
		execute_sudoku(sudoku)
		print_sudoku(sudoku)