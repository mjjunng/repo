# 실패, 시간초과 x
# def solution(scores):
#     wanho = scores[0]
#     scores.sort(key=lambda s: sum(s))
#     scores.reverse()
#     wanho_idx = scores.index(wanho)
#     rank = 1
#     for s in range(len(scores)):
#         if wanho[0] < scores[s][0] and wanho[1] < scores[s][1]:
#             return -1
#     for s in range(wanho_idx):
#         if wanho[0] < scores[s][0] and wanho[1] < scores[s][1]:
#             return -1
#         incentive = True
#         for i in range(len(scores)):
#             if scores[s][0] >= scores[i][0] or scores[s][1] >= scores[i][1]:
#                 break
#             if scores[s][0] < scores[i][0] or scores[s][1] < scores[i][1]:
#                 incentive = False
#                 break
#         if incentive:
#             rank += 1
#     return rank