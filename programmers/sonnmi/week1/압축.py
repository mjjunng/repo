def solution(msg):
    dict = {}
    for i in range(26):
        dict[chr(i+65)] = i+1
    answer = []
    begin = 0
    last = 1
    l = 26
    while begin < last and last <= len(msg):
        if msg[begin:last] in dict:
            tmp = msg[begin:last]
            found = False
            count = 0
            i = 0
            for ch in msg[last:]:
                tmp += ch
                i += 1
                if tmp in dict:
                    found = True
                    count = i
            if found:
                last = last + count
                answer.append(dict[msg[begin:last]])
                last += 1
            else:
                answer.append(dict[msg[begin:last]])
                last += 1
        else:
            tmp = msg[begin:last]
            found = False
            count = 0
            i = 0
            for ch in msg[last:]:
                tmp += ch
                i += 1
                if tmp in dict:
                    found = True
                    count = i
            if found:
                last = last + count
                answer.append(dict[msg[begin:last]])
                last += 1
            else:
                dict[msg[begin:last]] = l + 1
                l += 1
                begin = last - 1
    return answer