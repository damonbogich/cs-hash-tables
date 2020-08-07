# ignore: " : ; , . - + = / \ | [ ] { } ( ) * ^ &
ignore = [ '"', ":", ";", ",", ".", "-", "+", "/", "|", "[", "]", "(", ")", "*", "^", "&" ]
# ignore_symbol = "\"
#step 1: take a string and split it into list of seperate words, lowercase all words in list
sentence = "Damon likes basketball."
print(sentence.split())
split_sentence = sentence.split()
split_sentence = [i.lower() for i in split_sentence] #this lowercases everything in list
print(split_sentence) 




#how do i get rid of the special characters in my words??


# turn the split list into a dictionary:
count = 0
word_dictionary = dict.fromkeys(split_sentence, count)
print(word_dictionary)
#step 2: if the string contains any of the symbols that are in "ignore" list
    #make the dictionary keys all of the words in the list
    #their value should be the number of times that word is mentioned  

    #if the string does not contain any of the symbols that are in "ignore" list 
        #function should return an empty dictionary