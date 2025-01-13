import time
import os

def sumItemsRec(array: list) -> int:
    firstElementIndex = 0
    head = array.pop(firstElementIndex)
    tail = array

    # exit condition:
    if len(tail) == 0:
        return head
    return head + sumItemsRec(tail)

def printListRec(array: list):
    # destructing: https://blog.teclado.com/destructuring-in-python/
    head, *tail = array

    # pre-order: FIFO
    
    # in-order:
    if len(tail) > 0:
        printListRec(tail)
    # post-order: LIFO
    print(head)

numbers = list(range(0, 10))
#print(sumItemsRec(numbers))
printListRec(numbers)
exit()

def fibonacciRek(n: int): 
    if (n < 2):
        return n
    return fibonacciRek(n - 2) + fibonacciRek(n - 1)

# using storer to calculate faster, n = index
fibList = [0, 1]
def fibonacciRek_Storer(n: int): 
    if (n < len(fibList)):
        return fibList[n]
    result = fibonacciRek_Storer(n - 2) + fibonacciRek_Storer(n - 1)
    fibList.append(result)
    return result

#t0 = time.time()
#iteration = list(range(0, 300))
#for i in iteration:
#    print("i={0}: {1}".format(i, fibonacciRek_Storer(i)))
#t1 = time.time()
#print("execution time: {0}sec".format(t1 - t0))

#-------------------------------------------------
# Print folder structure

# return folders of the given path
def listFolder(path: str):
    """return folders of the given path"""
    list = os.listdir(path)
    list.sort()
    return list

def printFilesRec(path: str, prefix = ""):
    """ Az útvonalak tartalmának rekurzív kiíratása. """
    if prefix == "":
        print('list folder content')
        prefix = "| "

    folders = listFolder(path)
    for item in folders:
        # print line
        print(prefix + item)
        fullPath = os.path.join(path, item)

        # It is folder, start recursive it again
        if os.path.isdir(fullPath):
            printFilesRec(fullPath, prefix + "| ")

#printFilesRec("C:/Users/Sára Krisztián/Documents")