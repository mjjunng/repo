# https://school.programmers.co.kr/learn/courses/30/lessons/72414
# 참고: https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/#%EB%AC%B8%EC%A0%9C-5-%EA%B4%91%EA%B3%A0-%EC%82%BD%EC%9E%85

"""
누적합
N=[1,3*10^5]
O(N)
"""


def solution(play_time, adv_time, logs):

    def h_to_s(time: str):
        seconds = 3600
        t = list(map(int, time.split(":")))
        rst = 0
        for n in t:
            rst += int(n*seconds)
            seconds /= 60
        return rst

    def s_to_h(sec: int):
        s = sec % 60
        sec //= 60
        m = sec % 60
        sec //= 60
        h = sec
        return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)

    # 초로 변환
    play_sec = h_to_s(play_time)
    adv_sec = h_to_s(adv_time)
    logs_sec = []
    for t in logs:  # O(N)
        st, en = t.split("-")
        logs_sec.append((h_to_s(st), h_to_s(en)))

    # d 초기화 : d[i]= i 시각에 시청중인 사람의 수
    MAX_TIME = play_sec+1
    d = [0]*MAX_TIME
    for st, en in logs_sec:
        d[st] += 1
        d[en] -= 1

    # 시각별 시청자수 기록
    # d 재정의 : d[i]= 시각 i부터 i+1까지 1초 간의 구간을 포함하는 재생시간
    for i in range(1, MAX_TIME):
        d[i] += d[i-1]

    # 모든 시각 시청자수 누적 기록
    # d 재정의 : d[i]= 시각 0부터 i+1까지 i+1초 간의 구간을 포함하는 누적 재생시간
    for i in range(1, MAX_TIME):
        d[i] += d[i-1]

    # 정답 추출
    # 누적된 시청자수를 바탕으로 가장 시청자수가 많은 구간 탐색
    mx, idx = -1, 360010  # mx: 시청 누적 시간, idx: 가장 누적시간이 많은 시작 시각
    for i in range(adv_sec-1, MAX_TIME):
        if i >= adv_sec:
            if mx < d[i]-d[i-adv_sec]:  # 종료시각 - 시작시각 = 해당 구간 누적 재생수
                mx = d[i]-d[i-adv_sec]
                idx = i-adv_sec+1
        else:
            if mx < d[i]:
                mx = d[i]
                idx = i-adv_sec+1

    return s_to_h(idx)


play_time, adv_time, logs = "02:03:55", "00:14:15", [
    "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))

play_time, adv_time, logs = "99:59:59", "25:00:00", [
    "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))

play_time, adv_time, logs = "50:00:00", "50:00:00", [
    "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time, adv_time, logs))
