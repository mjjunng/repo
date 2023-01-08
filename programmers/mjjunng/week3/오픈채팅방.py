# implementation

def solution(record):
    answer = []
    data = {}   #data[id] : name
    
    for i in record:
        # 입장 
        if i.split()[0] == "Enter":
            data[i.split()[1]] = i.split()[2]
        # 닉네임 변경: data[id] = old_name -> data[id] = new_name 
        elif i.split()[0] == "Change":
            data[i.split()[1]] = i.split()[2]
        # 퇴장: 닉네임 변경한 경우 저장값 갱신해야 함  
        else:
            if i.split()[1] in data.items():
                data[i.split()[1]] = i.split()[2]
            
    for i in record:
        if i.split()[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(data[i.split()[1]]))
        elif i.split()[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(data[i.split()[1]]))


    return answer
