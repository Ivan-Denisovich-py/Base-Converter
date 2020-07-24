# Base converter. 10 to any; any to 10

import math

alpha=['A','B','C','D',
       'E','F','G','H',
       'I','J','K','L',
       'M','N','O','P',
       'Q','R','S','T',
       'U','V','W','X',
       'Y','Z']                         # # # Use isalpha()

# slicing function

def extract(n,f):   # n is a float
    whole=int(n)
    n=str(n)
    frac=float(n[len(str(whole)):len(str(whole))+1+f])
    return whole, frac          # whole in int, frac in float

# functions to convert to any

def convert_whole(n):
    out=''
    global base
    while n!=0:
        bit=str(n%base)
        if int(bit)>=10:
            bit=str(chr(int(bit)+55))
        out=bit+out
        n=n//base
    return out

def convert_frac(n):
    global base
    out=''
    i=0
    while n != 0:
        p=n*base
        q=int(p)
        if q>=10:
            q=str(chr(q+55))
        out+=str(q)
        n=extract(p, len(str(p))-(len(str(int(p)))+1))[1]
        i+=1
        if i==20:
            break
    return out

# functions to convert to decimal

def any_whole(n):               #inout data type: string
    out=0
    i=0
    global base
    while n!='':
        dig=n[-1:]
        if dig in alpha :
            dig=ord(dig)-55
        out+=int(dig)*int(math.pow(base,i))
        n=n[:-1]
        i+=1
    return out

def any_frac(n):        #input data type: string
    out=0
    i=1
    global base
    while n != '' :
        dig=n[:1]
        if dig in alpha :
            dig=ord(dig)-55
        out+=int(dig)*float(math.pow(base,-i))
        n=n[1:]
        i+=1
    return str(out)[2:]

print("This is a programme to convert base 10 numbers to other bases and vice versa.\n\n")
print('Please choose from the following conversions:')
print("a) Decimal to any base\nb) Any base to Decimal")
choice=input("[Enter a or b]:")
if choice == 'a':
    
# base 10 to any base
    num=float(input("Please enter a number in decimal: "))
    f=len(str(num))-len(str(int(num)))-1
    base=int(input("Input the base number you want it convert it to: "))
    output=str(convert_whole(extract(num, f)[0]))+'.'+str(convert_frac(extract(num, f)[1]))
    print('Your given number in base',base,'is:',output)

elif choice == 'b':
    
    base=int(input("Please enter the base number of your input: "))
    num=str(input("Please enter a number:"))
    
    fr=[]
    i, a=-1, num[-1]
    while a != '.':
        fr.append(a)
        i-=1
        a=num[i]
    f=len(fr)
      
    a1=str(any_whole(num[:(len(num)-f-1)]))
    a2=str(any_frac(num[-f:]))
    output=a1+'.'+a2
    print(output)
    
