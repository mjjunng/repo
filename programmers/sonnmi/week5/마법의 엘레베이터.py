def solution(storey):
    result = 0
    # 자릿수 숫자 끊어서 리스트에 담기
    splitStorey = list(map(int, str(storey)))
    # 자릿수 하나씩 봐줌
    for i in range(len(splitStorey)-1, -1, -1):
        # 이번 자릿수 >= 5
        if(splitStorey[i] > 5):
            if i == 0:
                result += 1
            result += 10-splitStorey[i]
            splitStorey[i-1] += 1
        # 마지막 자릿수가 아니고, 이번 자릿수 = 5, 다음 자릿수 5 이상이면
        elif i > 0 and splitStorey[i] == 5 and splitStorey[i-1] >= 5:
            result += 5
            splitStorey[i-1] += 1
        else:
            result += splitStorey[i]
    return result