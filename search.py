from operator import indexOf

arr = [11,22,33,44,55,66,77,88,99]
key: int = 77
start: int = 0
end =len(arr)
n = len(arr)-1
found: bool= False

for i in arr:
    if i == key:
        print("Found at ", indexOf(arr,i))
        break
while start <= end:
    mid = (start+end)//2
    if arr[mid] == key:
        print("Found element at index ", mid)
        found = True
        break
    elif key<arr[mid]:
        end = mid - 1
    else:
        start = mid + 1
if not found:
    print("Element not found")  n \