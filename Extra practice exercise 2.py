print("This is Practice Exeercises Extra 2")
print()
print("Exercise 1")
print()

n1 = 16
n2 = 24
gcd = 1

for k in range(2, min(n1,n2)+1):
    
    if n1 % k == 0 and n2 % k == 0 :
        gcd = k
        
print("The greatest common factor is:",gcd)

print()

n1 = 100
n2 = 250
gcd = 1
k = 2

while k <= n1 and k <= n2:
    
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
        
    k +=1
    
print("The greatest common factor is:",gcd)

print()
print("Exercise 2")
print()

n = 13
isPrime = True

if n <= 1:
    isPrime = False

for i in range(2, n):
    
    if n % 2 == 0:
        isPrime = False
        break
    
if isPrime:
    print("It is a prime number")
else:
    print("No, it is not a prime number")
        
print()
print("Exercise 3")
print()

def overlapping(a_list1, a_list2):
    
    for i in range(len(a_list1)):
        
        for j in range(len(a_list2)):
            
            if a_list1[i] == a_list2[j]:
                return True
            
    return False
            
list1 = [2,4,6,7,5]
list2 = [9.0,1,4,5]

overlap = overlapping(list1,list2)
print("Is it overlapping:",overlap)

print()
print("Exercise 4")
print()

def generateNchars(a_nNum, a_strChar):
    strr_x = ""
    
    for i in range(a_nNum):
        strr_x += a_strChar
        
    return strr_x

print("This generates:",generateNchars( 5, "x"))

print()

def histogram(a_listNum):
    
    for i in range(len(a_listNum)):
        strr_x = ""
        
        for j in range(a_listNum[i]):
            
            strr_x += "x"
            
        print(strr_x)
histo = [4,9,7]
histogram(histo)

print()
print("Exercise 5")
print()

def mapListTolength(a_listWords):
    list_len = []
    
    for i in range(len(a_listWords)):
        nLen = len(a_listWords[i])
        
        list_len.append(nLen)
    
    return list_len

def findLongestWord(a_listWords):
    
    len_word = mapListTolength(a_listWords)
    longest_len = 0
    
    for i in range(len(len_word)):
        
        if len_word[i] > longest_len:
            longest_len = len_word[i]
            
    return longest_len

listword = ["cat","banananana","jenny"]
print("The list of numbers:",mapListTolength(listword))
print("The longest lenth of the word is:",findLongestWord(listword))


print()
print("Exercise 6")
print()

def filterLongWords(a_listWords, a_nNum):
    list_longwords = []
    
    for i in range(len(a_listWords)):
        
        if len(a_listWords[i]) > a_nNum:
            list_longwords.append(a_listWords[i])
            
    return list_longwords
    
listwords = ["cat", "banana", "strawberry"]
print("The longer list of word is:",filterLongWords(listwords, 6))
            
print()
print("Exercise 7")
print()

def reverseList(a_listNum):
    list_reversed = []
    
    for i in range(len(a_listNum)-1,-1,-1):
        list_reversed.append(a_listNum[i])
    
    return list_reversed

listNum = [5,4,3,2,1,0]
print("The reversed list :",reverseList(listNum))

print()
print("Exercise 8")
print()

def isTriangular():
    listMatrix = [
        [3, 0, 0, 0, 0],
        [5, 2, 0, 0, 0],
        [1, 7, 4, 0, 0],
        [8, 5, 4, 1, 0],
        [2, 3, 1, 0, 2]
    ]
    nLen = len(listMatrix)
    
    for i in range(nLen):
        
        for j in range(i+1,nLen):
            
            if listMatrix[i][j] != 0:
                return False
            
        return True
    
print("Is it Triangular:",isTriangular())

print()
print("EXercise 9")
print()

def removeBiggerNum(list_nNum):
    nLen = len(list_nNum)
    
    for i in range(nLen):
        
        for j in range(i,nLen):
            print(list_nNum[j],end =" ")
        
        print()
    
    
nNum = [10,8,6,4,2,0]
removeBiggerNum(nNum)

print()
print("Exercise 10")
print()

def removeSmallestNum(list_nNum):
    nLen = len(list_nNum)
    
    for i in range(nLen):
        
        for j in range(nLen - i):
            print(list_nNum[j] ,end = " ")
            
        print()

nNum = [10,8,6,4,2,0]
removeSmallestNum(nNum)


print()
print("Exercise 11")
print()


def solveFarm():
    nHeads = 35
    nLegs = 94

    for i in range(nHeads + 1):
        nRabbits = i
        nChickens = nHeads - nRabbits

        if nRabbits * 4 + nChickens * 2 == nLegs:
            print("Rabbits:", nRabbits)
            print("Chickens:", nChickens)
            return


solveFarm()













































































































































































        