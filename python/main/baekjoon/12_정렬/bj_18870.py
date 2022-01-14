import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split())) # 2 4 -10 4 -9
sort_li = sorted(set(li)) # [-10, -9, 2, 4]
dic = { sort_li[i] : i for i in range(len(sort_li)) } # {-10: 0, -9: 1, 2: 2, 4: 3}

for i in li:
    print(dic[i], end=' ')

################################
# 시간초과 - index() 함수가 시간복잡도 높아서 dictionary 이용함

# n = int(input())
# li = list(map(int, input().split())) # 2 4 -10 4 -9
# sort_li = sorted(set(li)) # [-10, -9, 2, 4]
#
# for i in li:
#     idx = sort_li.index(i) <- 시간복잡도 O(N)
#     print(idx, end=' ')

# https://www.acmicpc.net/problem/18870 // 좌표압축

# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
#
# 입력
# 첫째 줄에 N이 주어진다.
#
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
#
# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
#
# 제한
# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109
# 예제 입력 1
# 5
# 2 4 -10 4 -9
# 예제 출력 1
# 2 3 0 3 1

# 예제 입력 2
# 6
# 1000 999 1000 999 1000 999
# 예제 출력 2
# 1 0 1 0 1 0