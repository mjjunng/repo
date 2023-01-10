import math

def solution(fees, records):
    answer = []
    standard_t = fees[0]
    standard_f = fees[1]
    unit_t = fees[2]
    unit_f = fees[3]
    result = {}

    for str in records:
        tmp = str.split()
        hours = int(tmp[0].split(":")[0])
        mins = int(tmp[0].split(":")[1])
        number = tmp[1]
        status = tmp[2]
        if not number in result:
            result[number] = {"sum": 0, "in_t": {"hours": hours, "mins": mins}, "status": False}
        else:
            if status == "OUT":
                result[number]["status"] = True
                in_t = result[number]["in_t"]["hours"] * 60 + result[number]["in_t"]["mins"]
                time = hours * 60 + mins - in_t
                result[number]["sum"] += time
            else:
                result[number]["status"] = False
                result[number]["in_t"]["hours"] = hours
                result[number]["in_t"]["mins"] = mins
    for number in sorted(result):
        if not result[number]["status"]:
            in_t = result[number]["in_t"]["hours"] * 60 + result[number]["in_t"]["mins"]
            result[number]["sum"] += 23 * 60 + 59 - in_t
        if result[number]["sum"] < standard_t:
            answer.append(standard_f)
        else:
            answer.append(standard_f + math.ceil((result[number]["sum"] - standard_t)/unit_t)*unit_f)
    return answer