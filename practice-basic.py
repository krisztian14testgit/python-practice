import time


"""
# Creating function
# Whice, for cycles
# Trivial types:
    - number: int, float, complex
    - string: str
    - boolean: bool
    - binary: bytes, bytearray
# complex types:
    - object
    - schangeable: list[], dictionary {}
    - immutable: tuple(val1, val2), set{halmaz, hal, ...}, frozenset

"""

#region List practising
"""
@input: 0 => mondey, 6 => sunday, -1 => None, 8 => None
@practise: len(): length of list
            range: range(startNumber, endNubmer, step number)
            for backward: for index in range(len(array)-1, -1, -1):
            for forward: for index in range(0, len(array), 1)
"""
def getDayNameBy(index):
    days = ['mondey', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if index > -1 and index < len(days):
        return days[index]
    
    return None

"""
@input: tuesday => 1, sunday => 6, adf => None

@practise: list.index(value): array.indexOf(value)
"""
def getIndexdDayby(day):
    days = ['mondey', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    retIndex = days.index(day)
    return retIndex if retIndex > 0 else None

"""
Traveling: startedDayNum: when you travel
            countedDaysNum: spending days
            get: which day will arriving
@input: (0, 5) => 5, saturday is arriving day
        (2, 14) => 2, wednesday is arriving day

@practise: abs(): math.abs
          int(number): type conversion
"""
def traveledDays(startedDayNum, countedDaysNum):
    numberOfWeek = 7
    restDays = countedDaysNum
    # more then 1 week counter
    if abs(countedDaysNum) >= numberOfWeek:
        weeks = int(countedDaysNum/numberOfWeek) # preserve integer
        restDays = countedDaysNum - weeks * numberOfWeek
    
    # one week counter
    result = startedDayNum + restDays
    if result >= numberOfWeek:
        return result - numberOfWeek

    if result < 0:
        return result + numberOfWeek
    return result

#dayIndex = traveledDays(2, 14)
#print(dayIndex)
#print(getDayNameBy(dayIndex))

"""
get mark of student by number
    90 => jeles
    80 => jó
    70 => Közepes
    60 => Elégséges
    0-59 => Elégtelen

@practise:   round(): math.round
            len(array): length of list
            rest division: %
            whole division: //
            string format: 'point: %f -> %s' %(x, mark)
"""
def getMarkBy(number):
    maxNum = 100.0
    marks = ['Jeles', 'Jó', 'Közepes', 'Elégséges', 'Elégtelen']

    subtracted = round(maxNum - number)
    # boundary numbers will get upper mark sign
    if subtracted % 10 == 0:
        subtracted -= 1
    
    index = subtracted // 10 # get integer number
    if index >= 5:
        index = len(marks) -1
    return marks[index]

# print(getMarkBy(45.9))
#xs = [89.7, 83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
#for x in xs:
#    mark = getMarkBy(x)
#    print('point: %f -> %s' %(x, mark))
#endregion
#----------------------------------------------------------
#region while cycle practise
numberList = [2,3,5,9,3,1]

def sumUntilFirstPositiveNum(list):
    i = 0
    isEvenNum = False
    summarized = 0
    while not isEvenNum and i < len(list):
        isEvenNum = list[i] % 2 == 0
        if (not isEvenNum):
            summarized += list[i]
        i += 1
    return summarized

"""
Triangle number: osszeadjuk az adott iteráció számlálóját
  0
 0 0
0 0 0
@input:  1. => 1
        2. => 1 + 2 = 3
        4. => 1 + 2 + 3 + 4 = 10
"""
def triangleNumbers(num):
    counter = 1
    summarized = 0
    while True:
        summarized += counter
        if counter >= num:
            break
        counter += 1
        
    return summarized

"""
Mennyi páros szám van a megadott számjegyben
pl: 123456 => 3 db (2,4,6)

@practise:   str(number): number to string
            int(value): string to number
"""
def evenDigitsCounter(num):
    evenCounter = 0
    strNum = str(num)
    i = 0
    while i < len(strNum):
        if int(strNum[i]) % 2 == 0:
            evenCounter += 1
        i += 1
    return evenCounter

#endregion
#-----------------------------------------------
#region String hangling

"""
Your own string.format() function
selfStringReplacement("az {0}, ez más: {1}, sas: {0}", 12, 'alma') => az 12, ez más: alma, sas: 12

@practise:   len()
            array.append(item) // array.push(item)
            text.split: "alma fa sas" => ["alma", "fa", "sas"]
            while
            slicing string
                * str[start-index, end-index, steps]
                * string[n:m]: substring
            "alma" + "fa" => "almafa"
"""
def selfStringReplacement(text = '', *args):
    signStart = '{'
    signEnd = '}'

    # collect indexes pos of replacement signs
    indexArray = []
    i = 0
    while i < len(text):
        if  (i + 1 < len(text) and i + 2 < len(text) and
            text[i] == signStart and text[i+2] == signEnd and text[i+1].isdigit()):
            charIndex = int(text[i+1])
            openBracketIndex = i
            closeBracketIndex = i + 2
            # ({,}, 0)
            indexArray.append( (openBracketIndex, closeBracketIndex, charIndex) )
        i += 1
    else:
        print('while-else:', i)
        print(indexArray)

    # Replace reference index to args' values
    retNewText = ''
    currentText = ''
    previousSubtext = ''
    splitText = text.split(signEnd)
    splitIndex = 0
    signEndRemoving = 1
    for record in indexArray:
        currentText = splitText[splitIndex] + signEnd
        # desructing like {id, name} = object
        # e.g.: (18, 20, 0) => posIndex => pozition of bracketValue {0}
        (startSignIndex, endSignIndex, posIndex) = record
        if len(retNewText) > 0:
            previousSubtext += splitText[splitIndex - 1] + signEnd
            startSignIndex -= len(previousSubtext)
            endSignIndex -= len(previousSubtext)

        retNewText +=  currentText[:startSignIndex]
        # "replacing number to inserting string"
        retNewText +=  str(args[posIndex])
        retNewText +=  currentText[endSignIndex + signEndRemoving:]

        splitIndex += 1

    remainString = splitText[len(splitText)-1]
    retNewText += remainString
    # ternalis: trueValue if condition else falseValue
    return retNewText if retNewText != '' else text

"""
Concetenation string pairs:
Törp + eros = Törperős
Törp + papan = Törpapa // one 'p' is skipped

@practise:   "ss" + "aa" => "ssaa"  
            substring:
            string[1:]: substring(startIndex, endIndex)
            string[1:3]: start to end index
            string[0:]: 0.index -> len(string)

            string split
            "Kis macska iszik".split() => ["Kis", "macska", "iszik"]
"""
def torp():
    elotag = "Törp"
    utotagok_listaja = ["eros", "költo", "morgó", "ölt˝o", "papa", "picur","szakáll"]
    for utotag in utotagok_listaja:
        if 'p' == utotag[0]:
            # substring(1, string.length)
            utotag = utotag[1:]
        print(elotag + utotag)

"""
@input: alma => amla
        sas => sas
"""
def reverseString(text):
    i = len(text) -1
    newString = ''
    while i > -1:
        newString += text[i]
        i -= 1
    else:
        print('last run:', i)
    return newString

"""
Szórzótábla megjelenítése

@exercise:   "fist: {0}, second: {1}".format(val1, val2) // c#: Console.log('{0} {1} {2}', val1, val2, val3)
            string formats:
            \t => tab
            f => float: .2f => two digits number
            x => hexadecimal
            {0:<12} => shift left + 12 space
            {0:>12} => shift right + 12 space
            {0:^12} => shift middle + 12 space
"""
def showMultiplicationTable(sizeNum):
    columns = ''
    for col in range(1, sizeNum + 1):
        columns += '\t' + str(col)
    print(columns)
    print("  :------------------------------------------------------------------------------------------")

    for col in range(1, sizeNum + 1):
        rowtxt = '{0} :'.format(col)
        if (len(str(col)) == 2):
            rowtxt = rowtxt[0:2] + rowtxt[3:]
        for row in range(1, sizeNum + 1):
            rowtxt += '\t' + str(col * row)
        print(rowtxt)

"""
@String conditions:
    abc order
    "alma" < "bananán" => true
    "zebra" < "alma" => false
    "c" in "cica" => true 
"""
#print(selfStringReplacement("az {0}, ez más: {1}, sas: {0}", 12, 'alma'))
#print(reverseString('farkas-kaland'))
#showMultiplicationTable(12)
#exit()
#endregion
#-------------------------------------------------------------------------------
#region List handling

"""
Replace the given char to new char
@input: Sapka => (p to l) => Salka

@practise:   enumerate(array): // js Object.entries()
            list(value) // to array
            string.join(stringArray): ["a", "s"] => "as"
"""
def replaceCharsIn(text, oldChar, newChar):
    text = str(text)
    textArr = list(text)
    for (index, value) in enumerate(textArr):
        if (value == oldChar):
            textArr[index] = newChar

    return "".join(textArr)

"""
Powers(i**2) items of array
numberPow(numberArray, exludedPositionIndexes)
    numberPow([1,2,3]) => [1, 4, 9]

@practise: deep copy array
          s = [] + array // get new array
          range(start, stop, step) / genereates number
          range(0,5) => Create a sequence of numbers from 0 to 5
          list(range(0,5)) => [0,1,2,3,4,5]
          array concat:
            array += [item, item2] => [..., item, item2]
          "-".join(["10","20","30"]) => "10-20-30"
"""
def numberPow(numbersArray, excludedPosArray = []):
    retArr = []
    exludedValues = []
    for index in range(0, len(numbersArray)):
        if (not index in excludedPosArray):
            retArr += [ numbersArray[index] ** 2 ]
        else:
            # array concetenation
            retArr += [numbersArray[index]] 
            exludedValues.append(str(numbersArray[index]))

    # return tuple
    return (retArr, "-".join(exludedValues))

#t0 = time.time()
#print(replaceCharsIn("ijkikaa", "ß", "z"))
#v = numberPow(list(range(1, 22, 3)), [0,5])
#t1 = time.time()
#print("tuple: {0}, time: {1}".format(v, t1-t0))
#exit()
# you cannot override the values of tuple
#v[1] = 2

def is_intiger(value: str) -> bool:
    """
    Inspect string value is intiger or not by ASCII code table
    numbers codes: 48 - 57

    @practise: ord(char): get ascii code of character
    @supported fn: text.isdigit() => returns True if all the characters are digits
    """
    for char in value:
        ascii_code = ord(char)
        if ascii_code < 48 or ascii_code > 57:
            return False
            
    return True

#print('int', is_intiger('111b')) # False

#endregion
#--------------------------------------------------------
#region **kwargs
# keywords argumenets: allows for any number of optional keyword arguments (parameters), which will be in a dict named kwargs.
def bar(**kwargs):
    for key in (kwargs):
        print(key, kwargs[key]) 

myDict = {'name': 12, 'adf': True}
for (key, v) in (myDict.items()):
    print(key, v)

#bar(name = 12)
#endregion
#-----------------------------------------------------------
#region dictionary task

"""
Counts letters in the string:
"almafa" => {a: 3, l: 1, m: 1, f:1}

@practise:  lower() // toLowerCase()
            iterate dict: for key, value in dict:
            string concatenate: c += 'fa'
            string.format()
"""
def countLetterIn(string: str) -> dict:
    dict = {}
    for char in string:
        lowerChar = char.lower()
        if lowerChar not in dict:
            dict[lowerChar] = 1
        dict[lowerChar] += 1
    return dict

def getCountedLetters(dictionary: dict) -> str:
    retString = '['
    for key, value in dictionary.items():
        retString += "{0}: count({1}), ".format(key, value)

    retString += ']'
    return retString

# myStr = "almafa"
# lettersDict = countLetterIn(myStr)
# print(getCountedLetters(lettersDict))

"""
Bubble sorting: 

@practise:  len(array)
            array.append(item)
            deep copy array: newArray = array[:]
"""
# sort dict element by the key in abc order, second max value by decreasing
def bubbleSorting2(sub_keyArray, originalDict):
    # collect values from dict by keys
    # keys: ['ab', 'ac'], 0 index refers key and value
    # values: [12, 20]
    valueArray = []
    # deep copy array
    keyArray = sub_keyArray[:] 
    for key in keyArray:
        valueArray.append(originalDict[key])

    i = len(valueArray) -1
    valueTemp = 0
    keyTemp = ''
    while i >= 0:
        j = 0
        while j <= i-1:
            #print('sss',valueArray[j], valueArray[j+1])
            # > => asceding
            # < => descreasing
            if (valueArray[j] > valueArray[j+1]):
                valueTemp = valueArray[j]
                valueArray[j] = valueArray[j+1]
                valueArray[j+1] = valueTemp

                keyTemp = keyArray[j]
                keyArray[j] = keyArray[j+1]
                keyArray[j+1] = keyTemp
                lastExhangeIndex = j
            j += 1
        #i = lastExhangeIndex
        i -= 1
    return (keyArray, valueArray)


"""
ascading order:
Sorting the dictionary by the key at first, after their values.
@input: {'abc': 10, 'zuu': 100, 'bcc': 50, 'bba':10, 'ss': 100, 'sa': 100, 'ss': 80} 
        ==> sorted: {'abc': 10, 'bba': 10, 'bcc': 50, 'ss': 80, 'sa': 100, 'zuu': 100}

@practise   dict.keys(): get keys from dictionary
            list(myDict.keys): dict keys to list
            array.sort: asceding sorting
            array.appned()
            zip(dictKeys, dictValue)
            dict(zip(keys, value))

"""
def sortingByABC_value(odict):
    keyArray = list(odict.keys())
    keyArray.sort()

    # create sub array by abc occurrence: abc, adg, az | c | z,zs => 3 db sub-array
    matrix = []
    newChar = 'a'
    subArray = []
    for key in keyArray:
        if (newChar != key[0]):
            matrix.append(subArray)
            subArray = []
        newChar = key[0]
        subArray.append(key)
    # add last sub-array content into matrix
    matrix.append(subArray)

    # there are more items in the array, should descarting them by number value
    dictKeys = []
    dictValues = []
    for keyArray in matrix:
        if (len(keyArray) > 1):
            # sorting by number
            (sortedKeys, sortedValues) = bubbleSorting2(keyArray, odict)
            dictKeys += sortedKeys
            dictValues += sortedValues
        else:
            # keyArray has only ONE element
            dictKeys += keyArray
            dictValues += [odict[keyArray[0]]]

    return dict(zip(dictKeys, dictValues))


#retDict = countLetterIn("Ez a Sztring Kis es Nagy Betuket tartalmaz")
#adict = {'abc': 10, 'zuu': 100, 'bcc': 50, 'bba':10, 'ss': 100, 'sa': 100, 'ss': 80}
#retDict = sortingByABC_value(adict)
#print(retDict)
#endregion
#----------------------------------------------------------------
#region Sequences:

fibStorer = [0, 1]
def fibonacchiRec(n):
    global fibStorer
    # existing condition
    if (n < len(fibStorer)):
        return fibStorer[n]
    newNum = fibonacchiRec(n-1) + fibonacchiRec(n-2)
    fibStorer = fibStorer + [newNum]
    return newNum

def factorialRec(n):
    #exit condition
    if n == 0:
        return 1
    return n * factorialRec(n-1)

# 1             if n = 1
# n/2,          if n is event number
# n * 3 + 1,    if n is odd
def collatzSequence(n):
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n * 3 + 1
        print('collatz: ', n)

def collatzSequenceReq(n, i):
    print('collatz({0}): {1}'.format(i,n))
    i += 1 # iteration num
    # exit condition
    if n == 1:
        return 1
    elif n % 2 == 0:
        n = collatzSequenceReq(n//2, i)
    else:
        n = collatzSequenceReq(3 * n + 1, i)

# Newton-sqrt: better = (appr + n/appr) / 2.0
def newtonSqrt(n):
    approximation = n / 2.0
    better = 0.0
    i = 0
    while True:
        better = (approximation + n/approximation) /2.0
        i += 1
        if abs(approximation-better) < 0.001:
            print('sqrt-iteration: ', i)
            return better
        approximation = better
        
def newtonSqrtRec(n, approximatly):
    better = (approximatly + n/approximatly) / 2.0
    #exit condition
    if abs(approximatly - better) < 0.001:
        return better
    approximately = better
    return newtonSqrtRec(n, approximately)


t0 = time.time()
for n in list(range(0,10)):
    print('fib({0})={1}'.format(n, factorialRec(n)))
#collatzSequenceReq(1000000, 0)
print('sqrt=', newtonSqrtRec(325689, 2500.0))
t1 = time.time()
print('executionTime=', t1-t0) # 9 sec
#endregion