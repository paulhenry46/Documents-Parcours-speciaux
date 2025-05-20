def newMax(a: float, b:float) -> float:
    if a >b:
        return a
    elif a<b:
        return b
    else:
        return a

def newMin(a: float, b:float) -> float:
    if a >b:
        return b
    elif a<b:
        return a
    else:
        return a
    
def maxArray(array: list) -> float:
    max = float(2)
    for i  in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max

def minArray(array: list) -> float:
    min = float(2)
    for i  in range(len(array)):
        if array[i] < min:
            min = array[i]
    return min


list = [1,2,58,-128,8]
print(maxArray(list))