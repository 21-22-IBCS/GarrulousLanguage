def selectionSort1(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.remove(minE)
        sortedList.append(minE)

    return sortedList

def sortNum(x):
    Min=0
    num=0

    for i in range(len(x)):
        Min=x[i]
        for j in range (i,len(x)):
            if (x[j]<Min):
                Min= x[j]
                num=j

        if (Min != x[i]):
            x[num]=x[i]
            x[i]=Min

    return x

def main():
    a=[2,5,3,21,1,100,25,40, 60, 9, 29, -2, 0, -10000000, 100000000, -100000000, 2]

    #print(selectionSort1(a))
    print(sortNum(a))
    

if __name__ == "__main__":
    main()
