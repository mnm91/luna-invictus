import string

def words():
    #Gives user choice of reading from a textfile or inputting text
    choice = input("Do want to read a textfile ('tf') or a text ('t')")
    
    #Puts the text into a variable called 'text'
    if choice == 'tf':
        textfile = input("Insert the name of the textfile")       
        file = open(textfile, 'rt')
        text = file.read()
        file.close()
    else:
        text = input("Insert text")
    
    #Makes text all lowercase
    text = text.lower()

    #removes punctuation
    table = string.maketrans(string.punctuation, '                                ')
    text = text.translate(table)

    
    split = text.split()
    text.replace(" ", "")
    split.sort()
    
    #Gets rid of duplicates
    single = [split[0]]
    for i in range(len(split)):
        if split[i] != single[len(single) - 1] :
            single.append(split[i])
    
    #Prints words in alphabetical order
    for word in single:
        print(word)
    
    return(single)
