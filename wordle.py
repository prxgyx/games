import enchant
import string
import time
from itertools import permutations
import itertools
from itertools import combinations
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import selenium
from selenium import webdriver

d = enchant.Dict("en_US")

all_letters_list = set(string.ascii_uppercase)

ruled_out_letters = set(["D", "U", "I", "B", "G", "L", "M", "V", "N"])
existing_letters_list = list(all_letters_list - ruled_out_letters)


five_letter_permutations = list(itertools.product(existing_letters_list, repeat=5))

for five_letter_permutation in five_letter_permutations:
	first_letter = five_letter_permutation[0]
	second_letter = five_letter_permutation[1]
	third_letter = five_letter_permutation[2]
	fourth_letter = five_letter_permutation[3]
	fifth_letter = five_letter_permutation[4]
	# print(five_letter_permutation)
	if fourth_letter == "E" and second_letter == "A":
		five_letter_word = "".join(five_letter_permutation)
		if d.check(five_letter_word):
			print(five_letter_word)
