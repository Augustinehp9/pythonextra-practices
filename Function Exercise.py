print()
print("Exercise 1")
print()

def showDouble(n):
    print("The double is:",n * 2)
    
num = showDouble(4)

print()
print("Exercise 2")
print()

def addSeven(n):
    n = n + 7
    return n

number = 5
print(addSeven(number))
print(number)

print()
print("Exercise 3")
print()

def addTwo(n):
    return n + 2

def triple(n):
    return n * 3
print("Triple is:",triple(addTwo(4)))

print()
print("Exercise 4")
print()

def isPositive(n):
    if n > 0:
        return True
    
    else:
        return False

print("The return is:",isPositive(-3))

print()
print("Exercise 5")
print()

def isMulitple(nNum, ndivisior):
    
    if nNum % ndivisior == 0:
        return True
    else:
        return False

print("The return is:",isMulitple(18,6),"because it is divisible. ")

print()
print("Exercise 6")
print()

def sumOneToN(a_nNum):
    total = 0
    
    for i in range(1,a_nNum+1):
        total += i
        
    return total

print("The sum is :",sumOneToN(5))

print()
print("Exercise 7")
print()

def countCharacter(a_strWord, a_strChar):
    count = 0
    
    for i in range(len(a_strWord)):
        if a_strChar in a_strWord[i]:
            count += 1
    return count
    
character = countCharacter("banana","a")
print("The char a in banana is:",character)

print()
print("Exercise 8")
print()

def isVowel(a_strChar):
    if a_strChar == "a" or a_strChar == "e" or a_strChar == "i" or a_strChar == "o" or a_strChar == "u":
        return True
    else:
        return False


def countVowels(a_strWord):
    count = 0
    
    for i in range(0,len(a_strWord)):
        if isVowel(a_strWord[i]):
            count += 1
            
    return count
    
print("Th num of vowels of education is:",countVowels("education"))
print("The num of vowels of sky is:",countVowels("sky"))

print()
print("Exercise 9")
print()

def digitcount(a_Num):
    count = 0
    
    if a_Num == 0:
        return 1
    
    while a_Num > 0:
        
        count += 1
        a_Num = a_Num // 10
        
    return count

print("The num of digit is:",digitcount(5492))
print("The num of digit is:",digitcount(0))

print()
print("Reverse Num Exercise")

def reverseNum(num):
    reverse = 0
    
    while num > 0:
        
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num//10
    
    return reverse

print("The reverse num is:",reverseNum(54321))


print()
print("Exercise 10")
print()

def isPalindromeWord(a_strWord):
    nLen = len(a_strWord)
    isPalindrome = True

    for i in range(0, nLen // 2):

        if a_strWord[i] != a_strWord[nLen - 1 - i]:
            isPalindrome = False
            break

    return isPalindrome


print("Is python palindrome?:", isPalindromeWord("python"))
print("Is levle palindrome?:", isPalindromeWord("level"))

print()
print("Exercise 11")
print()

def isEven(a_Num):
    
    if a_Num % 2 == 0:
        return True
    else:
        return False
    
def countEvenDigits(a_Num):
    count = 0
    
    while a_Num > 0:
        
        digit = a_Num % 10
        
        if isEven(digit):
            count += 1
         
        a_Num = a_Num // 10
        
    return count

print("Count of even numbers for 242345673:",countEvenDigits(242345673))
            
print()
print("Exercise 12")
print()

def isPerfectSquare(a_Num):

    for i in range(a_Num + 1):
        if i * i == a_Num:
            return True

    return False


def nextPerfectSquare(a_Num):
    num = a_Num + 1

    while isPerfectSquare(num) == False:
        num += 1

    return num


print("The next perfectsquare of 15 is:",nextPerfectSquare(15))
print("The next perfectsquare of 16 is:",nextPerfectSquare(16))
print("The next perfectsquare of 0 is:",nextPerfectSquare(0))

print()
print("Exercise 13")
print()

def countOverlapping(a_strtext, a_strsub):
    count = 0
    for i in range(len(a_strtext)):
        if a_strtext[i:i +len(a_strsub)] == a_strsub:
            count += 1
            
    return count

print("Count overlapping banana:",countOverlapping("banana","an"))
print("Count overlapping level:",countOverlapping("level","el"))

print()
print("Exercise 14")
print()

def isValidscore(a_score):
    
    if a_score <= 100 and a_score >= 0:
        return True
    
    return False

def gradeFromscore(a_score):
    
    if isValidscore(a_score) == False:
        return "Invalid"
        
    if a_score >= 90:
            return "A"
    elif a_score >= 80:
            return "B"
        
    elif a_score >= 70:
            return "C"
        
    elif a_score >= 60:
            return "D"
        
    else:
            return "F"
        
        
num = 99
print("Your final grade is:",gradeFromscore(num))


print()
print("Exercise 15")
print()

def sumDigits(a_num):
    sum = 0
    while a_num >0:
        digit = a_num % 10
        sum = sum + digit
        a_num = a_num // 10
        
    return sum

def digitalRoot(num):
  
    
    while num >= 10:
        num = sumDigits(num)
        
    return num

print("The digital root of 9875 is:",(digitalRoot(9875)))
print("The digital root of 7 is:",(digitalRoot(7)))
        
print()
print("Exercise 16")
print()

def resetList(a_listWord, a_Size, a_strValue):
    a_listWord.clear()
    
    for i in range(a_Size):
        a_listWord.append(a_strValue)
        
    return a_listWord

listWord = ["A","B"]
print(resetList(listWord, 7,"*"))

print()
print("Exercise 17")
print()

def resetList(a_nSize, a_strValue):
    listWord = []
    
    for i in range(a_nSize):
        listWord.append(a_strValue)
    
    return listWord

print(resetList(5, "%"))

print()
print("Exercise 18")
print()

def nlist(a_word):
    nLen = len(a_word)
    middle = nLen // 2
    if nLen % 2 == 0:
        newlist = a_word[:middle-1]+a_word[middle+1 :]
   
    else:
        newlist = a_word[:middle] + a_word[middle+1 :]
    
    return newlist

word = [1,2,3,4,5]
print("The output is:",nlist(word))

print()
print("Exercise 19")
print()

import random

def removeRandomCharacter(word):
    index = random.randrange(len(word))
    slice1 = word[0:index]
    slice2 = word[index + 1:]
    newword = slice1 + slice2
    print(newword)
    
word = "Python"
removeRandomCharacter(word)

print()
print("Exercise 20")
print()

def reverseWord(strword):
    nLen = len(strword)
    
    for i in range(nLen-1,-1,-1):
        print(strword[i],end = "")
        
word ="Education"
reverseWord(word)
        


















