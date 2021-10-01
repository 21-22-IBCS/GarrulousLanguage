#sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

#diff21
def diff21(n):
  if n<= 21:
    return (21-n)
  else:
    return (n-21)*2

#near_hundred
def near_hundred(n):
  if 110>=n>=90 or 210>=n>=190:
    return True
  else:
    return False

#missingchar
def missing_char(str, n):
  
  front = str[:n]
  back = str [n+1:]
  return front+back

#monkeytrouble
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    else:
        return False

#parrot_trouble
def parrot_trouble(talking, hour):
  if hour<7 or hour>20:
    return talking and True 
  else:
    return talking and False

#POS_NEG
    def pos_neg(a, b, negative):
  if (negative):
    if (a<0 and b <0):
      return True
    else:
      return False
  else:
    if (a>0 and b<0):
      return True 
    if (a<0 and b>0):
      return True 
    else:
      return False
    
#frontback
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

#sumdouble
def sum_double(a, b):
  if (a != b):
    return a+b 
  else:
    return (a+b)*2

#makes10
def makes10(a, b):
  if (a ==10 or b== 10):
    return True 
  if (a+b == 10):
    return True 
  else:
    return False

#notstring
def not_string(str):
  if ( str[:3] == "not"):
    return str
  else:
    str = "not "+str
    return str
#front3
def front3(str):
  if (len(str)>= 3):
    str= str[:3]+str[:3]+str[:3]
    return str
  else:
    str= str+str+str
    return str

