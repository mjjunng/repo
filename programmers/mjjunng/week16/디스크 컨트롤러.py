def solution(jobs):
    answer = 0
    start = 0
    n = len(jobs)
    jobs.sort(key=lambda x:x[1])
    
    while jobs:   
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                wait_time = start - jobs[i][0]
                answer += wait_time + jobs[i][1]
                start += jobs[i][1]
                jobs.pop(i)
                break
            
            # jobs에 있는 요청이 모두 현재 시간보다 클 때 시간 더해주어야 함 
            if i == len(jobs) - 1:
                start += 1
     
    return answer // n
