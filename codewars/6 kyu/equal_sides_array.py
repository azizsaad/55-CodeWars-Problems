arr = [1,2,3,4,5,6]

def find_even_index(arr):
    for i,x in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
        elif sum(arr[:i]) != sum(arr[i+1:]):
            i+1
    else:
        return -1

print (find_even_index([1,2,3,4,5,6]))
