
def findSumAndMultiply(numbers, sumto):
  for number in numbers:
    diff = sumto - number
    if diff in numbers:
      return diff * number
  return 0

def find2020SumWithThreeNumbers(numbers):
  for i in range(len(numbers)):
    diff = 2020 - numbers[i]
    multNum = findSumAndMultiply(numbers[:i] + numbers[i+1:], diff)
    if multNum != 0:
      return multNum * numbers[i]


  

reportFile = open("report.txt")
reportArray = reportFile.readlines()
numbers = [int(i) for i in reportArray]
numbers.sort()
print(findSumAndMultiply(numbers, 2020))
print(find2020SumWithThreeNumbers(numbers))