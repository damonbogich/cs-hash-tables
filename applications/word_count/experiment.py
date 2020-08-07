# ignore: " : ; , . - + = / \ | [ ] { } ( ) * ^ &
ignore = [ "\\", '"', ":", ";", ",", ".", "-", "+", "/", "|", "[", "]", "(", ")", "*", "^", "&", "=", "{", "}" ]

#step 1: take a string and split it into list of seperate words, lowercase all words in list
sentence = '":;,.-+=/\\|[]{}()*^&'
# split_sentence = sentence.split()
# split_sentence = [i.lower() for i in split_sentence] #this lowercases everything in list
# print(split_sentence)

for char in sentence:
    print(char)
    for j in ignore:
        if char.find(j) != -1:
            print(j)
            sentence = sentence.replace(j, '')
            print(sentence)
        # else:
        #     print('-1')
    
print(sentence)
# print(split_sentence)
split_sentence = sentence.split()
split_sentence = [i.lower() for i in split_sentence] #this lowercases everything in list
print(split_sentence)



word_dict = {}

for word in split_sentence:
    if word in word_dict:
        print('foundit')
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)

# one = 'on.e'
# two = '.'
# three = '!'
# four = 'p'

# print(one.find(four))