# 실패

# def solution(N, road, K):
#     # dict는 양방향 로드 최소 시간을 담는다
#     dict = {}
#     arr = [[] * i for i in range(N)]
#     for r in road:
#         a = r[0]
#         b = r[1]
#         if b not in arr[a - 1]:
#             arr[a - 1] += [b]
#         if a not in arr[b-1]:
#             arr[b - 1] += [a]
#         key = str(a) + str(b)
#         if key not in dict:
#             dict[key] = r[2]
#         else:
#             dict[key] = min(dict[key], r[2])
#     # 방문 가능한 모든 음식점을 담는다
#     visited = [1]
#     sol(dict, arr, 0, visited, [], 0, K)
#     return len(set(visited))
#
#
# def sol(dict, arr, arr_i, visited, visited_i, t, k):
#     if t > k:
#         return
#     if str(arr_i + 1) not in visited:
#         visited += [arr_i + 1]
#     for i in arr[arr_i]:
#         if i - 1 not in visited_i:
#             if str(arr_i + 1) + str(i) in dict:
#                 sol(dict, arr, i - 1, visited, visited_i + [arr_i], t + dict[str(arr_i + 1) + str(i)], k)
#             elif str(i) + str(arr_i + 1) in dict:
#                 sol(dict, arr, i - 1, visited, visited_i + [arr_i], t + dict[str(i) + str(arr_i + 1)], k)