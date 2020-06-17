def square_sum(k) :
    sum = 0

    digits = [int(i) for i in str(k)]
    for i in range(0, len(digits)) :
        sum += digits[i] * digits[i]
    if sum == 1 :
        return True
    elif sum == 0 or 0<=sum<=6:
        return False
    else :
        return square_sum(sum)


class Solution :
    def isHappy(self, n: int) -> bool :
        if n == 1 :
            return True
        elif n == 0:
            return False
        else :
            is_happy = square_sum(n)
            return is_happy


print(Solution().isHappy(1111111))
