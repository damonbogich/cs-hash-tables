# ignore: " : ; , . - + = / \ | [ ] { } ( ) * ^ &
ignore = [ '"', ":", ";", ",", ".", "-", "+", "/", "|", "[", "]", "(", ")", "*", "^", "&" ]
ignore_symbol = "\"
#step 1: take a string and split it into seperate words
    ## Any keys in the ignore list should not be put into dictionary
#step 2: 


def word_count(s):
    # Your code here



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))