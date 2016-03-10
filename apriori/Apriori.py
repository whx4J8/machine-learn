# coding=utf-8
from itertools import combinations, chain

debug = False


def loadData():
    return [[1, 3, 4, 5],
            [2, 3, 5],
            [1, 2, 3, 5],
            [1, 2, 3, 4, 5]]


def createC1(dataset):  # 创建一阶候选集
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)


def scan(data, itemSet, minSupport):  # 扫描频繁项集

    itemCountMap = {}
    for transaction in data:
        for item in itemSet:
            if item.issubset(transaction):
                if not itemCountMap.has_key(item):
                    itemCountMap[item] = 1
                else:
                    itemCountMap[item] += 1
    L1 = []
    supportData = {}
    totalCount = float(len(data))
    for key in itemCountMap:
        support = itemCountMap[key] / totalCount
        if support > minSupport:
            L1.insert(0, key)
            if debug: supportData[key] = support
        if not debug: supportData[key] = support

    return L1, supportData


def joinSet(itemSet, length):
    result = set()
    for i in itemSet:
        for j in itemSet:
            if len(i.union(j)) == length:
                result.add(i.union(j))
    return result


def subset(arr):
    return chain(*[combinations(arr,i+1) for i,a in enumerate(arr)])


def apriori(dataSet, minSupport=0.5):
    largeSet = {}  # 总的频繁项集
    largeSupport = {}

    c1 = createC1(dataSet)  # 创建一阶候选集
    l1, supportData = scan(map(set, dataSet), c1, minSupport)  # 扫描一阶频繁项集

    k = 2  # 下一阶k值
    currentLSet = l1  # 当前的频繁项集

    while currentLSet:
        largeSet[k - 2] = currentLSet  # store 当前频繁项集
        largeSupport = dict(largeSupport, **supportData)  # store 当前支持度

        currentCSet = joinSet(currentLSet, k)  # 获得k阶候选集
        currentLSet, supportData = scan(dataSet, currentCSet, minSupport)  # 扫描k阶候选集,得到频繁项集
        k += 1

    return largeSet, largeSupport


def rules(largeSet,largeSupport):

    rules = []
    for key,value in largeSet.items()[1:]:
        for item in value :
            subsets = map(frozenset,subset(item))
            for element in subsets :
                remain = item.difference(element)   #比较两个项集不同的地方
                if(len(remain) > 0):
                    confidence = largeSupport.get(item)/largeSupport.get(element)
                    rules.append((tuple(element),tuple(remain),confidence))
    return rules

if __name__ == '__main__':

    data = loadData()  # 加载交易数据
    largeSet, largeSupprt = apriori(data)
    rules = rules(largeSet, largeSupprt)
    for rule in rules :
        print rule





