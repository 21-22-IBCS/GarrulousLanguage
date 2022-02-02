def RTD(x):
    d = x/3.14159265359
    d = d*180

    return d

def ruleM(st):
    
    if (len(st) <= 3):
        return True

    for i in range(len(st)):
        if (st[i] == "c"):
            if (st[i+1] == "i"):
                if (st[i+2] == "e"):
                    return False

            else:
                if (st[i+1] == "e"):
                    if (st[i+2] == "i"):
                        return True
        else:
            if (st[i+1] == "i"):
                if (st[i+2] == "e"):
                    return True
                else:
                    return False
    return True
                        

def main():
    print(RTD(3.14))
    print(ruleM("believe"))
    print(ruleM("receipt"))
    print(ruleM("theif"))
    print(ruleM("cieling"))
    print(ruleM("banana"))


if __name__ == "__main__":
          main()
