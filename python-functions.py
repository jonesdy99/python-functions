## 1

# def sum_to(num):
#   sum = 0
#   for n in range(1, num + 1):
#     sum += n
#   return sum


# print (sum_to(6))



## 2
# def largest(nums):
#   largest = 0
#   for num in nums:
#     if num > largest:
#       largest = num
#   return largest


# print (largest([5,9,10,12,15,2,78,1]))


## 3

# def occurances(string, substr):
#   stripped_string = string.replace(substr, '')
#   return (len(string) - len(stripped_string)) // len(substr)

## 4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product