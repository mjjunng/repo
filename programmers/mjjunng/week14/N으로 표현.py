def solution(N, number):
    if number == 1:
        return 1

    dp = [0]   # dp[n]: N n개로 표현할 수 있는 집합 
    '''
    dp[1] = {5}
    dp[2] = {5+5, 5-5, 5//5, 5*5, 55} = {0, 1, 10, 25, 55}
    '''

    for i in range(1, 9):
        nums = set()
        nums.add(int(str(N) * i))
        for j in range(1, i//2+1):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    nums.add(op1 + op2)
                    nums.add(op1 * op2)
                    nums.add(op1 - op2)
                    nums.add(op2 - op1)
                    if op2 != 0:
                        nums.add(op1 // op2)
                    if op1 != 0:
                        nums.add(op2 // op1)
        if number in nums:
            return i
        dp.append(nums)

    return -1
