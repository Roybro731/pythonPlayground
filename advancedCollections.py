import collections

def namedTuple():
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 10)
    p2 = Point(20, 40)
    print(p1, p2.y)
    p1 = p1._replace(x=50)
    print(p1)

def defaultDic():
    """
        Example for default dictionary, no need to initialize array
    """
    arr = ["apple", "banana", "apple"]
    fruitCounter = collections.defaultdict(int)
    for fruit in arr:
        fruitCounter[fruit] += 1
    for key in fruitCounter:
        print("{0}:{1}".format(key, fruitCounter[key]))