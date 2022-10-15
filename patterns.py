def pattern1(n):
    for i in range(1,n+1):
         for j in range(1,i+1):
            print(j,end ='     ')
         print("\n")
    return 0

def pattern2(n):
        for i in range(1,n+1):
            for j in range (1,n-i+1):
                print(end='    ')
            for j in range(i,0,-1):
                print(j,end ='   ')
            for j in range(2,i+1):
                print(j,end = '     ')
            print('    ')


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
        for k in range(1,i):
            print("\t",end = '')
        for j in range(i,n+1):
            print(j,end = '\t')
        print("\n")
    return 0
def pattern6(n):
        for i in range(n):
            print()
            for j in range(n):
                if i == 0 or i == n-1 or j == 0 or j == n-2:
                    print('*',end = '   ')
                else: print('   ',end = '   ')
#pattern1(n)
# Driver code
ch = 'y'
while( ch=='y'):
    print("\n\t\tMENU\n (With reference to the word document)\n 1. Pattern (a)\n 2. Pattern (b)\n 3. Pattern (c)\n 4. Pattern (d)\n 5. Pattern (e)\n 6. Pattern (f)")
    a = int(input("\nEnter your choice: "))
    n = int(input("Enter the number: "))
    print()
    if a==1:
        pattern1(n)
    elif a == 2:
        pattern2(n)
    elif a == 3:
        pattern3(n)
    elif a == 4:
        pattern4(n)
    elif a == 5:
        pattern5(n)
    elif a == 6:
        pattern6(n)
    else: print("Abort Wrong choice!!")
    ch = input("\n Do you want to continue?(Y/n): ")
