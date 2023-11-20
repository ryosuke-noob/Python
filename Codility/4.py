import math



def solution(N):
    if 0 <= N and N <= 9:
        return 1
    n_str = str(N)
    num_size = len(n_str)
    count_0 = n_str.count('0')
    count_1 = n_str.count('1')
    count_2 = n_str.count('2')
    count_3 = n_str.count('3')
    count_4 = n_str.count('4')
    count_5 = n_str.count('5')
    count_6 = n_str.count('6')
    count_7 = n_str.count('7')
    count_8 = n_str.count('8')
    count_9 = n_str.count('9')
    ans = num_size - count_0
    ans *= math.factorial(num_size - 1)
    ans /= math.factorial(count_0)
    ans /= math.factorial(count_1)
    ans /= math.factorial(count_2)
    ans /= math.factorial(count_3)
    ans /= math.factorial(count_4)
    ans /= math.factorial(count_5)
    ans /= math.factorial(count_6)
    ans /= math.factorial(count_7)
    ans /= math.factorial(count_8)
    ans /= math.factorial(count_9)
    
    return int(ans)

n = int(input())
print(solution(n))