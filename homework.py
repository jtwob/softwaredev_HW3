def addArray(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum

def multArray(arr):
    product = 1
    for i in arr:
        product*=i
    return product

def reverseArray(arr):
    return list(reversed(arr))
        

def main():
    len = input("How long is the array: ")

    arr = [int(x) for x in input("Enter " + len + " values separated by spaces: ").split()]

    print("Sum: " + str(addArray(arr)))
    print("Product: " + str(multArray(arr)))
    print("Reversed: ", reverseArray(arr))

main()
    