#given a string, count the number of times a letter occurs
example_string = 'The quick brown fox jumps over the lazy dog'


#remove spaces and throw it all into a list
string_list = example_string.split()
print(string_list)
giant_string = "".join(string_list)
print(giant_string)

letter_counts = {}
#iterate over giant string, 
for letter in giant_string:
    letter = letter.lower()

# check if letter is in dictionary
    if letter in letter_counts:

# if it is increment count,
        letter_counts[letter] += 1
# if not add
    else:
        letter_counts[letter] = 1



# print each letter, starting with the most common, down to the least common

print(letter_counts)

sorted_letter_counts = sorted(letter_counts.items(), key=lambda pair: pair[1], reverse=True)

for pair in sorted_letter_counts:
    print(pair[0])

