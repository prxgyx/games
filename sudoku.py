from multipledispatch import dispatch
from dataclasses import dataclass
from typing import List


ALLOWED_VALUES = set(range(1,10))


@dataclass
class Pencil:
    value: List[int]

def check_if_sudoku_is_valid(sudoku):
	for rid in range(0, 9):
		for cid in range(0, 9):
			elem = sudoku[rid][cid]
			rcb_values = get_rcb_values(rid, cid, sudoku)
			print(elem)
			print(rcb_values)
			if isinstance(elem, int):
				elem = set([elem])
			if elem.issubset(rcb_values):
				print_sudoku(sudoku)
				raise Exception("Something wrong in row - {} and col {}".format(rid+1, cid+1))



def init_array():
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
	# for i in range(0, 9):
	# 	sudoku[i] = [0] * 9
	return sudoku

def print_sudoku(sudoku):
	for row in sudoku:
		print(*row, sep = "  ")

# def convert_pencil_to_final(pencil):
# 	if len(pencil.value) == 1:
# 		return pencil.value[0]

def check_if_value_is_int(value):
	return isinstance(value, int)

def get_row_values(rid, sudoku):
	row_values = [elm for elm in sudoku[rid] if check_if_value_is_int(elm)]
	# print(row_values)
	return set(row_values)

def get_col_values(cid, sudoku):
	col_values = []
	for row in sudoku:
		col_value = row[cid]
		if check_if_value_is_int(col_value):
			col_values.append(col_value)
	return set(col_values)

'''
bid - block id
blocks =
1	2	3
4	5	6
7	8	9
'''
def get_bid(rid, cid):
	# rid = 0, 1, 2
	if rid < 3:
		# cid = 0, 1 ,2
		if cid <3:
			return 1
		# cid = 3, 4, 5
		elif cid >= 3 and cid <6:
			return 2
		# cid = 6, 7, 8
		else:
			return 3
	# rid = 3, 4, 5
	elif rid >=3 and rid <6:
		# cid = 0, 1 ,2
		if cid <3:
			return 4
		# cid = 3, 4, 5
		elif cid >= 3 and cid <6:
			return 5
		# cid = 6, 7, 8
		else:
			return 6
	# rid = 6, 7, 8
	else:
		# cid = 0, 1 ,2
		if cid <3:
			return 7
		# cid = 3, 4, 5
		elif cid >= 3 and cid <6:
			return 8
		# cid = 6, 7, 8
		else:
			return 9

# @dispatch(int, int)
def get_block_value(bid, sudoku):
	block_values = []

	bid_value_dict = {
	1: (range(0,3), range(0,3)),
	2: (range(0,3), range(3,6)),
	3: (range(0,3), range(6, 9)),
	4: (range(3,6), range(0, 3)),
	5: (range(3,6), range(3, 6)),
	6: (range(3,6), range(6, 9)),
	7: (range(6, 9), range(0, 3)),
	8: (range(6, 9), range(3, 6)),
	9: (range(6, 9), range(6, 9))
	}

	rid_cid_values = bid_value_dict[bid]

	rid_range = rid_cid_values[0]
	cid_range = rid_cid_values[1]

	for rid in rid_range:
		for cid in cid_range:
			block_value = sudoku[rid][cid]
			if check_if_value_is_int(block_value):
				block_values.append(block_value)

	return set(block_values)

# @dispatch(int, int, List[int])
def get_block_values(rid, cid, sudoku):
	bid = get_bid(rid, cid)
	block_values = get_block_value(bid, sudoku)
	return block_values

# rcb - row, column, block
def get_rcb_values(rid, cid, sudoku):
	row_values = get_row_values(rid, sudoku)
	col_values = get_col_values(cid, sudoku)
	block_values = get_block_values(rid, cid, sudoku)

	return set().union(row_values, col_values, block_values)

def get_pencil_value(rid, cid, sudoku):
	rcb_values = get_rcb_values(rid, cid, sudoku)
	pencil_values = ALLOWED_VALUES - rcb_values
	if pencil_values == set():
		print_sudoku(sudoku)
		raise Exception("Empty set for row {} and column {} - Last correct state".format(rid+1, cid+1))
	return pencil_values

def write_pencil_values(sudoku):
	for rid in range(0, 9):
		for cid in range(0,9):
			elem = sudoku[rid][cid]
			if elem == 0 or not isinstance(elem, int):
				sudoku[rid][cid] = get_pencil_value(rid, cid, sudoku)
	return sudoku

def convert_pencil_values_to_solution(sudoku, state_change):
	for rid in range(0, 9):
		for cid in range(0,9):
			possible_pencil_value = sudoku[rid][cid]
			# print(possible_pencil_value)
			if not isinstance(possible_pencil_value, int) and len(possible_pencil_value) == 1:
				# print("possible_pencil_value", possible_pencil_value)
				sudoku[rid][cid] = next(iter(possible_pencil_value))
				state_change = True
				# print(state_change)
	return state_change

def execute_sudoku(sudoku):

	state_change = True

	while state_change:
		state_change = False
		write_pencil_values(sudoku)
		# print("Write pencil_values")
		# print_sudoku(sudoku)
		state_change = convert_pencil_values_to_solution(sudoku, state_change)
		# check_if_sudoku_is_valid(sudoku)
		# print("state_change", state_change)
		# print_sudoku(sudoku)


if __name__ == "__main__":
	sudoku = init_array()
	execute_sudoku(sudoku)
	print_sudoku(sudoku)