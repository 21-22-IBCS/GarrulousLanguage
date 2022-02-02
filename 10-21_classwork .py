def main():

    #Create a list
    #hold multiple data objects in python
    fruits = ["apples", "banana", "kiwis", "mangos"]
    anotherList= ["string", 14, -2.3, True]
    listOfLists= ["check", "this", "out", ["a", "list"]]

    aList= list(("soccer", "badminton", "photography", "theater","weight-lifting"))
    print(aList)
    #length of list
    x = len(fruits)

    #outputing list
    print(fruits)
    print(anotherList)
    print(listOfLists)

    bList = []
    #add elements to a list
    bList.append("Adam Sandler")
    bList.append("Ronaldo")
    bList.append("Jeff Bezos")
    bList.append("Ms. Corrigan")
    bList.append("Ronaldo")
    bList.append("Ronaldo")
    print(bList)

    #iteration through lists and their indexes
    print(bList[0])
    print("A soccer player i do not like is "+bList[2])
    print(bList[-1])

    #subists can be accessed through indexes
    print(bList[1:3])
    print(bList[:2])
    print(bList[3:])

    #conditions involving lists

    if "Ronaldo" in bList:
        print("yuck!")
    if 4 in bList:
        print("a number here")

    #loop through lists
        
    for celeb in bList:
        print(celeb)

    for i in range(len(bList)):
        print(i)
        print(bList[i])

    
    #how many Ronaldo can we romove??????
    bList.remove("Ronaldo")
    print(bList)

    #remove the 4th element
    bList.pop(3)
    print(bList)

    #set elements equal to new data values
    bList[1]= "Pogba"
    print(bList)

    nList = [3, 2, 4, 6, 10, 13, 12]
    nList.sort()
    print(nList)
            


if __name__ == "__main__":
    main()
