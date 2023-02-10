
# 실패
# import copy
#
#
# t = [list(map(int, input().split())) for i in range(4)]
# a = [[t[i][j] for j in range(0, 8, 2)] for i in range(4)]
# b = [[t[i][j]-1 for j in range(1, 8, 2)] for i in range(4)]
#
# # [행, 렬]
# dd = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
# d_n = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
# # 크기가 작은 물고기 순으로 위치를 배열에 저장 (크기는 1-16 중복 없이 있음)
# idx_ = [0] * 16
# for i in range(4):
#     for j in range(4):
#         idx_[a[i][j]-1] = [i, j]
#
# visited = []
# # idx_[a[0][0]-1] = [-1, -1]
# # a[0][0] = -1
# s_idx = [0, 0]
# s_d = b[0][0]
# # b[0][0] = -100000
#
#
# def dfs(a_, b_, s_idx, s_d, m, cnt, in_dx_, visited):
#     mx = 0
#     print()
#     # 물고기 이동
#     in_dx = copy.deepcopy(in_dx_)
#     a = [r[:] for r in a_]
#     a[s_idx[0]][s_idx[1]] = -1
#     b = copy.deepcopy(b_)
#     for i in range(16):
#         # 물고기가 있을 경우
#         if 0 <= in_dx[i][0] < 4 and 0 <= in_dx[i][1] < 4 and a[in_dx[i][0]][in_dx[i][1]] != -1:
#             # 45도씩 회전하면서 제일 먼저 나오는 방향으로 이동
#             d_cnt = 0
#             # 이동시킬 물고기의 방향
#             d = b[in_dx[i][0]][in_dx[i][1]]
#             while d_cnt < 8:
#                 if d == 8:
#                     d = 0
#                 # 이동하려는 위치
#                 cur_y = in_dx[i][0]+d_n[d][0]
#                 cur_x = in_dx[i][1]+d_n[d][1]
#                 # 물고기가 이동하려는 구간이 상어의 위치이거나 4x4 구간 안에 있어야 함
#                 if (cur_y != s_idx[0] or cur_x != s_idx[1]) and (0 <= cur_x < 4 and 0 <= cur_y < 4):
#                     printLoc(a, b)
#                     print()
#                     # 이동하려는 위치의 물고기 숫자
#                     cur_n = a[cur_y][cur_x]
#                     # 이동 가능한 구간의 물고기 숫자
#                     # 이동 가능하기 때문에 현재 물고기의 위치와 바꾸려는 위치를 교환
#                     temp = [in_dx[i][0], in_dx[i][1]]
#                     temp_a = a[temp[0]][temp[1]]
#                     cur_a = a[cur_y][cur_x]
#                     # temp_b = b[temp[0]][temp[1]]
#                     temp_b = d
#                     cur_b = b[cur_y][cur_x]
#                     # cur_b = d
#                     in_dx[i] = [cur_y, cur_x]
#                     print(a[temp[0]][temp[1]])
#                     # 물고기 위치 교환
#                     a[temp[0]][temp[1]] = cur_a
#                     a[cur_y][cur_x] = temp_a
#                     # 물고기 방향 교환
#                     b[temp[0]][temp[1]] = cur_b
#                     b[cur_y][cur_x] = temp_b
#                     # 물고기 숫자로 정렬된 1차원 배열도 갱신한다
#                     in_dx[cur_n-1] = [temp[0], temp[1]]
#                     break
#                 d_cnt += 1
#                 d += 1
#     print("_____")
#     # 상어 이동
#     # 한 번에 여러 칸을 이동할 수 있기 때문에 이동할 수 있는 방향으로 갈 수 있는 모든 경우를 봐줌
#     print(s_d >= 8)
#     temp_s = [s_idx[0], s_idx[1]]
#     while 0 <= temp_s[0] < 4 and 0 <= temp_s[1] < 4:
#         if a[temp_s[0]][temp_s[1]] != -1:
#             # 상어가 물고기를 잡음
#             val = a[temp_s[0]][temp_s[1]]
#             in_dx[a[temp_s[0]][temp_s[1]]-1] = [-10, -10]
#             print("==", b[temp_s[0]][temp_s[1]])
#             ans = val + dfs(a, b, temp_s, b[temp_s[0]][temp_s[1]], m + in_dx[temp_s[0]*4 + temp_s[1]], cnt+1, in_dx, visited + m)
#             if ans > mx:
#                 mx = ans
#         temp_s[0] += d_n[s_d][0]
#         temp_s[1] += d_n[s_d][1]
#     return mx
#
#
# def printLoc(a, b):
#     for i in range(len(a)):
#         for j in range(len(b)):
#             print((a[i][j],dd[b[i][j]]), end=" ")
#         print()
# print(dfs(a, b, s_idx, s_d, [], 0, idx_, []))