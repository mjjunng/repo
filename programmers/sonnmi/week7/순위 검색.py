# 1번째 시도
# 효율성 0
# def solution(info, query):
#     answer = []
#     # info_ = info[:]
#     # 모든 문자열 공백으로 띄워서 리스트에 저장
#     for i in range(len(info)):
#         info[i] = info[i].split()
#
#     # 쿼리 개수만큼
#     for qr in query:
#         q = qr.split(" and ")
#         temp = q[3].split()
#         q[3] = temp[0]
#         q += [temp[1]]
#         cnt = 0
#         # 조건 해당하는 사람 수 answer에 순서대로 담기
#         for p in info:
#             satisfy = True
#             if int(q[4]) > int(p[4]):
#                 satisfy = False
#             if satisfy:
#                 for i in range(4):
#                     if q[i] != "-" and q[i] != p[i]:
#                         satisfy = False
#                         break
#             if satisfy:
#                 cnt += 1
#         answer += [cnt]
#     return answer


# 2번째 시도 - 일반 테스트, 효율성 다 실패함
# map 을 만들어서 (점수가 key) 점수를 기준으로 sort 해서 나중에 이진탐색으로 점수 조건 맞는 사람을 구한다


# def solution(info, query):
#     answer = []
#     d = {}
#     # 모든 문자열 공백으로 띄워서 query 형식으로 mapping
#     for i in range(len(info)):
#         info[i] = info[i].split()
#         if int(info[i][4]) not in d:
#             d[int(info[i][4])] = []
#         # d[int(info[i][4])] += [" and ".join(info[i][:4])]
#         d[int(info[i][4])] += [info[i][:4]]
#     d = sorted(d.items())
#
#     # 쿼리 개수만큼
#     for qr in query:
#         q = qr.split(" and ")
#         temp = q[3].split()
#         q[3] = temp[0]
#         q += [temp[1]]
#         cnt = 0
#
#         # 이진탐색
#         start = 0
#         end = len(d) - 1
#         mid = 1
#         while start <= end:
#             mid = (start + end) // 2
#             if d[mid][0] == int(q[4]):
#                 break
#             elif d[mid][0] < int(q[4]):
#                 start = mid + 1
#             else:
#                 end = mid - 1
#                 if mid - 1 >= 0 and d[mid - 1][0] < int(q[4]):
#                     break
#         # mid는 d[mid][0] >= 조건 점수
#         # 조건 해당하는 사람 수 answer에 순서대로 담기
#         for i in range(mid, len(d)):
#             for p in d[i][1]:
#                 satisfy = True
#                 for s in range(4):
#                     if q[s] != "-" and q[s] not in p:
#                         satisfy = False
#                 if satisfy:
#                     cnt += 1
#         answer += [cnt]
#     return answer
