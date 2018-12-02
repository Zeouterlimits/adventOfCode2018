import collections


def isPositive(num):
    if num[0:1] == '+':
        return True


def stripPositivityIndicator(num):
    return int(num[1:])


def addToFrequencyPairResultset(pairResult):
    countOfPairResult = resultsDictionary.get(pairResult)

    if type(countOfPairResult) == int:
        countOfPairResult += 1
        if countOfPairResult > 1:
            raise Exception(" found! " + str(pairResult))
    else:
        countOfPairResult = 1

    resultsDictionary[pairResult] = countOfPairResult


def iterateThroughFileAndSum(filepath, sum):
    sumOfCurrentPair = 0

    # map with per line result as key
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            currentInputValue = line.strip()
            if isPositive(currentInputValue):
                sumOfCurrentPair = sum + \
                    stripPositivityIndicator(currentInputValue)
                addToFrequencyPairResultset(sumOfCurrentPair)
                sum = sumOfCurrentPair
            else:
                sumOfCurrentPair = sum - \
                    stripPositivityIndicator(currentInputValue)
                addToFrequencyPairResultset(sumOfCurrentPair)
                sum = sumOfCurrentPair
            line = fp.readline()
            sumOfCurrentPair = 0

    return sum


def main():
    filepath = 'input.txt'
    sum = 0

    while success != True:
        sum = iterateThroughFileAndSum(filepath, sum)


# Global Scope
resultsDictionary = collections.Counter()
success = False
main()
