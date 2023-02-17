# DP


def toInt(time):
    time = time.split(":")
    hour = int(time[0]) * 3600
    minute = int(time[1]) * 60
    second = int(time[2])

    return hour + minute + second


def toStr(time):
    hour = addZero(str(time // 3600))
    minute = addZero(str(time % 3600 // 60))
    second = addZero(str(time % 3600 % 60))
    return hour + ":" + minute + ":" + second


def addZero(time):
    if len(time) == 1:
        return "0" + time
    return time


def solution(play_time, adv_time, logs):
    # 동영상 재생시간만큼 공간 만들기
    dp = [0] * (toInt(play_time) + 1)

    # 모든 시청자 재생 구간에 대해서
    for i in logs:
        # 시작 시간과 끝나는 시간을 구하기
        temp = i.split('-')
        start = toInt(temp[0])
        end = toInt(temp[1])
        # 시작점과 끝나는 점을 마크
        dp[start] += 1
        dp[end] -= 1
    # 광고 재생 시작 시간부터 끝나는 시간전까지 다 1이 되게 한다
    # (1로 구분해서) 시작 시간부터 끝나는 시간을 알 수 있음
    for i in range(1, toInt(play_time)):
        dp[i] = dp[i] + dp[i - 1]
    # 누적 값을 구하기 위해 한 번 더 돌린다
    for i in range(1, toInt(play_time)):
        dp[i] = dp[i] + dp[i - 1]

    mx = -1
    answer = 0
    # 제일 많은 누적 수를 찾는다
    # adv_time 간격만큼 봐주니까 adv_time 부터 시작하면 된다
    for i in range(toInt(adv_time) - 1, toInt(play_time)):
        temp = dp[i] - dp[i - toInt(adv_time)]
        if temp > mx:
            mx = temp
            answer = i - toInt(adv_time) + 1

    return toStr(answer)