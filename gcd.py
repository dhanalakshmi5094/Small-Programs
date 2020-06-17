def generalizedGCD(num, arr) :
    # WRITE YOUR CODE HERE
    if num != len(arr) :
        print("Please enter list of numbers same to num given")
    elif len(arr) <= 1 :
        return arr
    else :
        for i in range(len(arr) - 1) :
            a = arr[i]
            b = arr[i + 1]
            while b :
                a, b = b, b % a
            arr[i + 1] = a
        return a


print(generalizedGCD(5, [5, 10, 80, 45, 5]))