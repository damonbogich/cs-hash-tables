import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # print(words) #prints everything from file

#split into words
split_words = words.split() #splits all of the words into a list
print(split_words)

# TODO: analyze which words can follow other words
# Your code here
dataset = {}

#populates dataset with all of the words and the words that follow them
for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in dataset:
        dataset[word] = [next_word]
    
    else:
        dataset[word].append[next_word]

#make a list of start words
## if first or second character is capitalized put it into list
## Loop over split words and put any start word into the list

##can add a .keys() to your hashtable
start_words = []
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

#random start word:
word = random.choice(start_words)

# TODO: construct 5 random sentences
# Your code here

stopped = False

stop_signs = "?.!"

while not stopped:
    #print the word
    print(word)

    #if it's a stop word stop:
    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        stopped = True

    #choose a random following word
    following_words = dataset[word]

    word = random.choice(following_words)
