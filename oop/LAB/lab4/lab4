file_name='a.txt'
def counter(file_name):
    num_words=0
    num_lines=0
    num_symbols=0
    num_spaces=0
    with open (file_name,'r') as f:
        for line in f:
            num_lines+=1    
        for letter in line:
            if (letter==' '  ):
                num_spaces+=1
            num_words=num_spaces+1
            if(letter !=' ' and letter !='\n'):
                num_symbols+=1
    print("Number of lines  in a given text file:",num_lines)
    print("Number of words in a given text file:",num_words)
    print("Number of spaces in a given text file:",num_spaces)
    print("Number of symbols in a given text file:",num_symbols)
 
counter(file_name)