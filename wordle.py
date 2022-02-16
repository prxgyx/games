import enchant
import string
from itertools import permutations

d = enchant.Dict("en_US")

all_letters_list = set(string.ascii_uppercase)

# existing_letters_list = ["Q", "W", "Y", "F", "J", "Z", "X", "C", "V", "B", "N", "I"]

ruled_out_letters = set(["E", "R", "I", "S", "D", "N", "V"])
existing_letters_list = list(all_letters_list - ruled_out_letters)


# three_letter_permutations = list(permutations(existing_letters_list, 4))

# for three_letter_permutation in three_letter_permutations:
# 	trial_four_letter_word = "".join(three_letter_permutation) + "I"

# 	for l in existing_letters_list:
# 		trial_five_letter__word = trial_four_letter_word + l

# 		if d.check(trial_five_letter__word):
# 			print(trial_five_letter__word)



# three_letter_permutations = list(permutations(existing_letters_list, 4))

# for three_letter_permutation in three_letter_permutations:
# 	trial_four_letter_word = "".join(three_letter_permutation) + "I"

# 	for l in existing_letters_list:
# 		trial_five_letter__word = trial_four_letter_word + l

# 		if d.check(trial_five_letter__word):
# 			print(trial_five_letter__word)



five_letter_permutations = list(permutations(existing_letters_list, 5))

for five_letter_permutation in five_letter_permutations:
	first_letter = five_letter_permutation[0]
	second_letter = five_letter_permutation[1]
	third_letter = five_letter_permutation[2]
	fourth_letter = five_letter_permutation[3]
	fifth_letter = five_letter_permutation[4]
	if "U" in five_letter_permutation and "A" in five_letter_permutation and "L" in five_letter_permutation:
		if first_letter != "L" and first_letter != "A":
			if second_letter != "U":
				if third_letter != "A":
					if fourth_letter != "A":
						if fifth_letter != "U":
							five_letter_word = "".join(five_letter_permutation)
							if d.check(five_letter_word):
								print(five_letter_word)
