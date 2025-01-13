# Fibonacci (előző szomszédos számok összege), + reck
# 0,                ha n = 0
# 1,                ha n = 1
# f(n-1) + f(n-2),  ha n >= 2
def fibonacciNumbers(n):
    n0 = 0
    n1 = 1
    i = 1 # start runnig form 2. cycle
    newNum = n
    while i < n:
        newNum = n0 + n1
        n0 = n1
        n1 = newNum
        i += 1
    return newNum
    
def fibonacciRec(n):
    # exit condition
    if n < 2:
        return n
    return fibonacciRec(n-1) + fibonacciRec(n-2)
    
# storing the previous counted number in recursive function to be faster
fibStore = [0, 1]
def fibonacciRec2(n):
    # exit condition
    if n < len(fibStore):
        return fibStore[n]
    newNum = fibonacciRec2(n-1) + fibonacciRec2(n-2)
    fibStore.append(newNum)
    return newNum

for n in list(range(0,10)):
    print('fib({0})={1}'.format(n, fibonacciNumbers(n)))
    
#-----------------------------------------------------
# faktoriális számítás
# 1             ha n < 2
# n * f(n-1),   ha n > 1
def factorial(n):
    multiNum = 1
    i = 1
    while i <= n:
        multiNum *= i
        i += 1
    return multiNum

# n! = n * (n-1) * (n-2)*... * 1
def factorialRec(n):
    # exit condition
    if n < 2:
        return 1
    return n * factorialRec(n-1)

# storing calculated numbers to be executed rapidly
factStorer = [1, 1]
def factorialRec2(n):
    if n < len(factStorer):
        return factStorer[n]
    m = n * factorialRec2(n-1)
    factStorer.append(m)
    return m
#--------------------------------------------------------
# Collatz-sorozat
# 1             if n = 1, exit condition
# n/2,          if n is event number -> divide 2
# n * 3 + 1,    if n is odd
def collatzSequence(n):
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n * 3 + 1
        print('collatz: ', n)

# in recursively
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
   
#-------------------------------------------------------
# newton négyzetgyök(quare root) számítás
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

# in recursively
def newtonSqrtRec(n, approximatly):
    better = (approximatly + n/approximatly) / 2.0
    #exit condition
    if abs(approximatly - better) < 0.001:
        return better
    approximately = better
    return newtonSqrtRec(n, approximately)


# buborék rendezés: javított 1,2 version