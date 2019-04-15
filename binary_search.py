'''递归实现'''
def binary_search_1(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binary_search_1(alist[:midpoint],item)
          else:
            return binary_search_1(alist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search_1(testlist, 3))
print(binary_search_1(testlist, 13))

'''非递归实现'''
def binary_search_2(alist, item):
      first = 0
      last = len(alist)-1
      while first<=last:
          midpoint = (first + last)//2
          if alist[midpoint] == item:
              return True
          elif item < alist[midpoint]:
              last = midpoint-1
          else:
              first = midpoint+1
    return False
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search_2(testlist, 3))
print(binary_search_2(testlist, 13))

