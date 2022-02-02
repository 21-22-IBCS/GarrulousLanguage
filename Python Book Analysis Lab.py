def main():
    f = open("Alice.txt", "r")
    fulltext = f.read()
    listOfText = fulltext.split(" ")
    start= 0
    end= 0
    
    
    while not ("CHAPTER" in listOfText[start]):
        start=start+1
        
    while not ("ILLUSTRATIONS" in listOfText[end]) and not ("REPRODUCED" in listOfText[end+1]):
        end = end+1

    newText =[]
    for i in range (start+1,end-2):
        newText.append(listOfText[i])

    #average text length   
    n= 0
    avg= 0
    for i in range(len(newText)):
        n= n+ len(newText[i])
    avg= n/ len(newText)

    print("The average word length of the text is "+ str(avg)+".")
    print("\n")
     
    #most common word
    dictionary={}
    for i in newText:
        if not (i == ""):
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
 
    maximum= 0   
    commonWord=""
    for key in dictionary:
        if dictionary[key]>maximum:
            maximum=dictionary[key]
            commonWord=key
             
    print("The most common word in the text is: "+commonWord +".")
    print("\n")

    #percentage of the text
    newLine=[]
    for i in newText:
        if not (i == ""):
            newLine.append(i)

    total=len(newLine)

    ptgOr= (dictionary["or"]/ total)*100
    ptgAnd= (dictionary["and"]/ total)*100
    ptgBut= (dictionary["but"]/ total)*100

    print("The percentage of 'and' in the text is "+str(ptgAnd)+ "%.")
    print("The percentage of 'but' in the text is "+str(ptgBut)+ "%.")
    print("The percentage of 'or' in the text is "+str(ptgOr)+ "%.")
    print("\n")

    #longest sentence in the text
    listOfSentence= fulltext.split("!")
    listOfSen2=[]
    for i in listOfSentence:
        listOfSen2+= i.split("?")
    listOfSen3=[]
    for i in listOfSen2:
        listOfSen3+= i.split(".")
    listOfSen5=[]
    for i in listOfSen3:
        listOfSen5+= i.split(";")
    
    for i in listOfSen5:
        i=i.replace("\n"," ")
    
        
        
    start2=0
    end2=0


    while (not ("CHAPTER I" in listOfSen5[start2])):
        start2= start2+1
        
        
        
    while not ("ILLUSTRATIONS REPRODUCED BY HENTSCHEL COLOURTYPE" in listOfSen5[end2]):
        end2= end2+1



    newSentence =[]
    for i in range (start2,end2-1):
        newSentence.append(listOfSen5[i])

    max3=0
    sentc=""
    for i in newSentence:
        if len(i)>max3:
            max3=len(i)
            sentc=i

    print("The longest sentence in the text is: "+sentc)
    

if __name__ == "__main__":
    main() 
