import datetime
import enum

#region Geogebra-practice
class Axis(enum.Enum):
    X = 0
    Y = 1
    Z = 2

class Point:

    @staticmethod
    def getS() -> str:
        return ""

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def getDistanceFrom(self, p1) -> float:
        return ((self.x - p1.x)**2 + (self.y - p1.y)**2) ** 0.5

    def reflectToAxis(self, axis: Axis):
        if axis == Axis.X:
            return Point(self.x, self.y * -1)
        elif axis == Axis.Y:
            return Point(self.x * -1, self.y)

    # origótol mért meredekség: gradiens of line
    def getSlopeFromOrigo(self) -> float:
        # arra mutat amerre a point van
        iranyVektor = Point(self.x, self.y)
        # m = v2 / v1; iranyVektor(v1, v2)
        return iranyVektor.y / iranyVektor.x if iranyVektor.x != 0 else 0.0
        
    # help: questio4 = https://www.geeksforgeeks.org/point-gradient-formula/
    def getStraightLine(self, point) -> tuple:
        # egyenes egyenlete: y - y1 = m(x -x1)
        # get meredekség: (p2.y - p1.y) / (p2.x - p1.x)
        slope = (point.y - self.y) / (point.x - self.x)
        # y = m(x - x1) + y1
        x = slope # m*x
        y = slope * -1 * point.x + point.y
        return (x, y)

#p1 = Point(4, 11)
#p2 = Point(6, 15)
#dist = p1.getDistanceFrom(p2)
#slope = p2.getSlopeFromOrigo()
#egynesTuple = p1.getStraightLine(p2)
#print(egynesTuple)
#endregion
#-------------------------------------------------
#region SMS üezenet gyakorlat

class SMS:
    isReaded: bool
    sentNumbers: int
    arrivalTime: datetime
    text: str

    def __init__(self, sentNumbers: int, arrivalTime: datetime, text: str):
        self.isReaded = False
        self.sentNumbers = sentNumbers
        self.arrivalTime = arrivalTime
        self.text = text

    # convert object to string,
    # it will be called by print(),
    # type conversion: str()
    def __str__(self) -> str:
        return "({0}, {1}, {2}, {3})".format(self.isReaded, self.sentNumbers, self.arrivalTime, self.text)

class SMSStorer:
    _storer: list = []

    def addText(self, sentNumbers: int, arrivalTime: datetime, text: str):
        sms = SMS(sentNumbers, arrivalTime, text)
        self._storer.append(sms)

    def getCount(self) -> int:
        return len(self._storer)
    
    # return indexes of the unread texts
    def getUnreadText_indexes(self) -> list:
        retList = []
        for i in range(0, len(self._storer)):
            # add unread text into list
            if not self._storer[i].isReaded:
                retList.append(i)
        
        return retList
        
    def getSMSBy(self, index: int) -> tuple:
        if index > 0 and index < len(self._storer):
            sms: SMS = self._storer[index]
            sms.isReaded = True
            return (sms.isReaded, sms.sentNumbers, sms.arrivalTime, sms.text)

        
        return None

    # print the sms_storer by the print function or str type
    def __str__(self):
        retString = "sms_storer: \n"
        for index in range(len(self._storer)):
            retString += "{0} => {1}, \n".format(str(index), str(self._storer[index]))
        return retString

# instance of SMSStorer
bejovo_uzenetek = SMSStorer()
# creating 3 sms_text
for db in range(3):
    bejovo_uzenetek.addText(10, datetime.time(), "text1")
length = bejovo_uzenetek.getCount()
# one text is opened and read
smsTuple = bejovo_uzenetek.getSMSBy(1)
print("get SMS:", smsTuple)
unreadIndexes = bejovo_uzenetek.getUnreadText_indexes()
print("unread text index: ", unreadIndexes)
print(bejovo_uzenetek)
#endregion
#----------------------------------------------

#region class- iterators object exmaple
# source: https://www.programiz.com/python-programming/iterator
class MySumNumbers:
    def __init__(self, maxIterationNum: int):
        self.max = maxIterationNum
        self._sum = 0

    # intialize the first element of the iterators
    def __iter__(self):
        self.n = 0 # set beginner value
        return self

    def __next__(self):
        print('Current element: ', self.n)
        # Exit condition of the Python infinite operators
        if self.n > self.max:
            raise StopIteration
            #raise SystemError('Exit condition of the Python infinite operators')
            #exit()
        
        self._sum += self.n
        self.n +=1
        return self.n

    @property
    def Sum(self) -> int:
        return self._sum

    # setter property
    @Sum.setter
    def Sum(self, value: int):
        if value > 0:
            self._sum = value
        else:
            raise SystemError('Value not be negative!')


print('print sum')
c = MySumNumbers(10)
item = iter(c)
print(next(item))
print(next(item))
print(next(item))

# for cycle on the iterators
for n in c:
    print(n)

#endregion
#------------------------------------
#region Make property decorator
# sources:
# https://python101.pythonlibrary.org/chapter25_decorators.html
# https://www.programiz.com/python-programming/property
class Temp:
    _degrees = 0.0

    def getDegrees(self) -> float:
        return self._degrees

    def setDegrees(self, value):
        self._degrees = value

    # property(fget=None, fset=None, fdel=None, doc=None)
    Degress = property(getDegrees, setDegrees)
    # ----------------------------------------------
    # 2. Creating property with decorator
    # getter property
    @property
    def NegDegrees(self) -> int:
        return self._degrees

    # setter property
    @NegDegrees.setter
    def NegDegrees(self, value: int): # func name must be same with @property
        if value < 0:
            self._degrees = value
        else:
            raise SystemError('Have to be negative!')

#temp = Temp()
#s = temp.getDegrees()
#temp.NegDegrees = -10
#print('Degrees:', temp.NegDegrees)

"""
Default @decorators:
    - @classmethod
    - @staticmethod
    - @property

    source: https://python101.pythonlibrary.org/chapter25_decorators.html
"""
#endregion