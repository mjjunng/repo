"""
1. 시간 초과 FAIL, 문제 해석 X

BRUTEFORCE
- 모든 시간을 정수 값으로 변환하여 연산
- play_time -> 거대 배열
- logs -> xxx-yyy 해당 인덱스의 count ++
- 해당 배열 adv_time 구간 단위로 돌면서 최대 count 값 pick !

def solution(play_time, adv_time, logs):
    # 동영상 전체 구간 연산
    ph, pm, ps = map(int, play_time.split(':'))
    plen = ph * 60 * 60 + pm * 60 + ps
    total_time = [0] * (plen + 1)  # 전체 시간 배열

    # logs -> 구간 정수화 -> 해당 배열에 count ++
    for log in logs:
        str_st, str_et = log.split('-')
        # 시작 시각 처리
        sh, sm, ss = map(int, str_st.split(':'))
        st = sh * 60 * 60 + sm * 60 + ss
        # 끝나는 시각 처리
        eh, em, es = map(int, str_et.split(':'))
        et = eh * 60 * 60 + em * 60 + es

        for i in range(st, et + 1):
            total_time[i] += 1

    # adv_time 구간을 옮겨 가며 최대 count 합 check
    ah, am, asec = map(int, adv_time.split(':'))
    alen = ah * 60 * 60 + am * 60 + asec
    max_time = -float('inf')
    ans_start_time_n = 0
    for st in range(plen - alen):
        time_sum = sum(total_time[st: st + alen + 1])
        if time_sum > max_time:
            max_time = time_sum
            ans_start_time_n = st

    # 시간 형식 변환
    ans_s = ans_start_time_n % 60
    ans_h, ans_m = divmod((ans_start_time_n - ans_s) // 60, 60)

    return str(ans_h).zfill(2) + ":" + str(ans_m).zfill(2) + ":" + str(ans_s).zfill(2)
"""

"""
2. 풀이 참고
https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/#%EB%AC%B8%EC%A0%9C-5-%EA%B4%91%EA%B3%A0-%EC%82%BD%EC%9E%85
https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.3-%EA%B4%91%EA%B3%A0-%EC%82%BD%EC%9E%85-JS

누적합 (PREFIX SUM)
- refactor : 시간 형식 변환 함수 1) 문자열 시간 -> 정수형 시간 / 2) 정수형 시간 -> 문자열 시간
- total_time 2차례 누적합 거쳐서 누적 재생 횟수 배열 만들기
    1) (초기 배열) total_time[x] : x초에 시작된 재생 구간 개수 - x초에 끝난 재생 구간 개수
    2) (누적합 배열) total_time[x] : x초의 시청자 수
    3) (누적합 배열) total_time[x] : x초의 누적 재생 수
- total_time[끝] - total_time[시작] -> 최대 재생 시간 구간 갱신
"""


def time_str_to_int(time_str):
    HH, mm, ss = map(int, time_str.split(':'))
    return HH * 3600 + mm * 60 + ss


def time_int_to_str(time_int):
    ss = time_int % 60
    HH, mm = divmod((time_int - ss) // 60, 60)

    return str(HH).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)


def solution(play_time, adv_time, logs):
    play_time, adv_time = time_str_to_int(play_time), time_str_to_int(adv_time)
    total_time = [0] * (play_time + 1)

    # log 시작, 끝 시각 활용 -> 초기 total_time 만들기
    for log in logs:
        st, et = log.split('-')
        st, et = time_str_to_int(st), time_str_to_int(et)  # 시작, 끝
        total_time[st] += 1
        total_time[et] -= 1

    # 누적합 배열 만들기 1 -> 시청자 수
    for i in range(1, play_time + 1):
        total_time[i] += total_time[i - 1]

    # 누적합 배열 만들기 2 -> 누적 재생 시간
    for i in range(1, play_time + 1):
        total_time[i] += total_time[i - 1]

    # total_time 활용해 MAX 누적 재생 시간인 구간 구하기
    max_time = -float('inf')
    start_time = 0
    for e in range(adv_time, play_time + 1):
        cur_time = total_time[e - 1] - total_time[e - adv_time - 1]  # 구간 주의,, -> 이상 - 미만
        if cur_time > max_time:
            max_time = cur_time
            start_time = e - adv_time

    return time_int_to_str(start_time)


print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))

# 9, 31 TC 실패
