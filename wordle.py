import enchant
import string
from itertools import permutations

d = enchant.Dict("en_US")

all_letters_list = list(string.ascii_lowercase)

existing_letters_list = ["Q", "W", "Y", "F", "J", "Z", "X", "C", "V", "B", "N", "I"]

# As my word is _ _ _ I _
three_letter_permutations = list(permutations(existing_letters_list, 3))

for three_letter_permutation in three_letter_permutations:
	trial_four_letter_word = "".join(three_letter_permutation) + "I"

	for l in existing_letters_list:
		trial_five_letter__word = trial_four_letter_word + l

		if d.check(trial_five_letter__word):
			print(trial_five_letter__word)



