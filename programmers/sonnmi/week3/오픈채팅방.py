def solution(record):
    answer = []
    d = {}
    for i in range(len(record)):
        cmd = record[i].split()[0]
        if cmd != "Leave":
            id = record[i].split()[1]
            name = record[i].split()[2]
            if id not in d:
                d[id] = name
            else:
                d[id] = name
    for i in range(len(record)):
        cmd = record[i].split()[0]
        id = record[i].split()[1]
        if cmd == "Enter":
            answer.append(d[id] + "님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(d[id] + "님이 나갔습니다.")
    return answer