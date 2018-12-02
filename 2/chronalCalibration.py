

def isPositive(num):
    if num[0:1] == '+':
        return True

def stripPositivityIndicator(num):
    return int(num[1:])


filepath = 'input.txt'  
sum = 0
currentFrequency = 0
resultsDictionary = {0:0}

# map with per line result as key
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       currentInputValue = line.strip()
       if isPositive(currentInputValue) :
        currentFrequency = sum + stripPositivityIndicator(currentInputValue)
        resultsDictionary[currentFrequency] = resultsDictionary[currentFrequency] + 1
        # Key Error 11 - https://wiki.python.org/moin/KeyError
        sum = currentFrequency
       else:
        currentFrequency = sum - stripPositivityIndicator(currentInputValue)
        sum = currentFrequency
       print("Current Value {}: {}".format(cnt,sum))
       line = fp.readline()
       cnt += 1
       currentFrequency = 0

