

def isPositive(num):
    if num[0:1] == '+':
        return True

def stripPositivityIndicator(num):
    return int(num[1:])


filepath = 'input.txt'  
sum = 0
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       currentValue = line.strip()
       if isPositive(currentValue) :
        sum = sum + stripPositivityIndicator(currentValue)
       else:
        sum = sum - stripPositivityIndicator(currentValue)
       print("Current Value {}: {}".format(cnt,sum))
       line = fp.readline()
       cnt += 1

