def binarySearch (array1, l, r, x): 
  
    if r >= l: 
  
        mid = l + (r - l)/2
  
        if array1[mid] == x: 
            return mid 
           
        elif array1[mid] > x: 
            return binarySearch(array1, l, mid-1, x) 
  
        else: 
            return binarySearch(array1, mid + 1, r, x) 
  
    else: 
        return -1
        
print("enter the elements of the list")
array1=list(mao(int,input().split()))
x=input("enter the element to be searched")
result = binarySearch(array1, 0, len(array1)-1, x) 
  
if result != -1: 
    print "Element is present in the array") 
else: 
    print ("Element is not present in array")
