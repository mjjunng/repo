from collections import defaultdict
import math


def solution(fees, records):
    # 누적 시간 업데이트 하기
    total_time = defaultdict(int)  # 차량별 누적 시간
    record_stack = defaultdict(list)  # 입차 기록 스택
    for record in records:
        time, car_num, stat = record.split()
        hours, mins = map(int, time.split(':'))
        if stat == "IN":
            record_stack[car_num].append(hours * 60 + mins)
        else:
            total_time[car_num] += (hours * 60 + mins - record_stack[car_num].pop())
    # 스택에 남은 기록이 있다면 출차하지 않은 차량 -> 처리 필요
    for car_num in record_stack.keys():
        if record_stack[car_num]:
            total_time[car_num] += (23 * 60 + 59 - record_stack[car_num].pop())

    # 주차 요금 계산
    res = []
    for _, times in sorted(total_time.items()):
        if times <= fees[0]:
            res.append(fees[1])
        else:
            total_fee = fees[1] + math.ceil((times - fees[0]) / fees[2]) * fees[3]
            res.append(total_fee)

    return res


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
