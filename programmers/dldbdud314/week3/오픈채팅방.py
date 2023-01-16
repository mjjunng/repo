'''
구현
time : record 길이: n -> O(2 * n)

1. record 돌면서 Enter/Change에 따른 닉네임 저장
2. record 돌면서 Enter/Leave에 따른 result 반영
'''


def solution(record):
    # 닉네임 저장
    names = dict()  # names[uid] = nickname
    for x in record:
        stat = x.split()
        if stat[0] == "Enter" or stat[0] == "Change":
            names[stat[1]] = stat[2]

    # result(최종 결과) 반영
    result = []
    for x in record:
        stat = x.split()
        if stat[0] == "Enter":
            result.append(names[stat[1]] + "님이 들어왔습니다.")
        elif stat[0] == "Leave":
            result.append(names[stat[1]] + "님이 나갔습니다.")

    return result
