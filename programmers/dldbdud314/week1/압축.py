def solution(msg):
    dictionary = {chr(i + 64): i for i in range(1, 27)}  # 사전 초기화
    last = len(dictionary)  # 색인 추가용

    res = []
    cur_idx = 0
    index = -1  # 존재하는 단어의 마지막 색인 저장
    while cur_idx < len(msg):
        for jump in range(1, len(msg) + 1):
            word = msg[cur_idx:cur_idx+jump]
            if word in dictionary:
                index = dictionary[word]
            else:
                last += 1
                dictionary[word] = last  # 사전 업데이트
                res.append(index)
                index = -1
                cur_idx += (jump - 1)
                break
        else:
            res.append(index)
            break

    return res


print(solution("A"))