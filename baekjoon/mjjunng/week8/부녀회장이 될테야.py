# implementation-O(n^3)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    t = int(input())
    info = [[0 for _ in range(15)] for _ in range(15)]  #info[k][n] : k층 n호에 거주하고 있는 인원

    # 0층 거주민 초기화
    for i in range(15):
        info[0][i] = i

    # 1층 ~ 14층 거주민 초기화
    for i in range(1, 15):
        for j in range(1, 15):
            for k in range(1, j+1):
                info[i][j] += info[i-1][k]

    for _ in range(t):
        k = int(input())
        n = int(input())

        print(info[k][n])
