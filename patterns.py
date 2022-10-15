def pattern1(n):
    for i in range(1,n+1):
         for j in range(1,i+1):
            print(j,end ='     ')
         print("\n")
    return 0

#def pattern2(n):


def pattern3(n):
    for i in reversed(range(1,n+1)):
         for j in reversed(range(1,i+1)):
            print(j,end ='     ')
         print("\n")
    return 0

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end ='     ')
        print("\n")
    return 0
def pattern5(n):
    for i in range(1,n+1):
        for k in range(2,n+1):
            print(' ',end =' ')
        for j in range(i,n+1):
            print(j,end = ' ')
        #for k in range(1,n):
        #   print(k,end = ' ')
        print()
    return 0
n = int(input("Enter the number: "))
pattern5(n)
#pattern1(n)