#Math game: every number leads to 8.

first_number = input('choose a number between 1 - 9 :')   #ask the user to choose a number bet1ween 1 - 9.

first_number = int(first_number)     #input() returns a string, so we use int() to convert it to an integer.

number = first_number   #Assign number to first_number for calculations.
number *= 2
number += 8
number += first_number
number -= 2
number /= 3
number -= first_number
number *= 4

print(number)

# ──────────────────────────────
#   💻 Code by Mahsa ✨
#   📅 2025
# ──────────────────────────────



