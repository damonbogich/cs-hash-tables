# ignore: " : ; , . - + = / \ | [ ] { } ( ) * ^ &

#step 1: take a string and split it into list of seperate words
    
#step 2: if the string contains any of the symbols that are in "ignore" list
    #make the dictionary keys all of the words in the list
    #their value should be the number of times that they are 

    #if the string does not contain any of the symbols that are in "ignore" list 
        #function should return an empty dictionary

def word_count(s):
    ignore = [ "\\", '"', ":", ";", ",", ".", "-", "+", "/", "|", "[", "]", "(", ")", "*", "^", "&", "=", "{", "}" ]
    for char in s:
        print(char)
        for j in ignore:
            if char.find(j) != -1:
                
                s = s.replace(j, '')
            else:
                print('-1')

    split_sentence = s.split()
    split_sentence = [i.lower() for i in split_sentence] #this lowercases everything in list
    print(split_sentence)



    word_dict = {}

    for word in split_sentence:
        if word in word_dict:
            print('foundit')
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))