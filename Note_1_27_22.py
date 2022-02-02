def main():
    #String data type
    word = "apple"
    empty = ""
    large = "The quick brown fox jumps over the lazy dog."
    empty2= str()
    print(empty2)

    #split example
    sentence = "I like python."
    splitSentence= sentence.split("y")
    print(splitSentence)

    #strip example
    favorite= "ssocscers"
    print(favorite)
    newFav=favorite.strip("s")
    print(newFav)

    #text files
    f = open("Alice.txt", "r")
    '''fulltext = f.read()
    listOfText = fulltext.split(" ")'''
    for i in range(15):
        print(f.readline())

    #iterate through a loop (2 ways)
    '''for i in range(len(listOfText)):
        print(listOfText[i])
        for k in range(len(listOfText)):
            print(listOfText[k][0])

    for w in listOfText:
        print(w)'''
        

    
    

if __name__ == "__main__":
    main() 
