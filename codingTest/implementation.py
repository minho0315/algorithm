# 구현
# 1.아이디어를 코드로 바꾸는 구현
# 예제 4-1 상하좌우
# n = int(input())
# m = list(map(chr, input().split()))
# print(m)

# 문제 해설
# N을 입력받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
#
# print(x, y)


# 예제 4-2. 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 구하여라
# n = int(input())
# count = 0
#
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if i%10 == 3:
#                 count+=1
#                 continue
#             if j%10 == 3 or j//10 == 3:
#                 count+=1
#                 continue
#             if k%10 == 3 or k//10 == 3:
#                 count+=1
#                 continue
# print(count)

# 문제 해설
# H를 입력받기
# h = int(input())
#
# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) + str(k):
#                 # '000' 부터 시작
#                 count += 1
#
# print(count)

# 2. 왕실의 나이트
# 문제의 핵심 : 8 x 8 체스판에서 나이트는 특정한 방법(수평으로 두 칸 이동한 뒤에 수직으로 한칸 이동 or 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동)으로 움직인다.
# 체스판의 위치를 입력했을 때 나이트가 움직일 수 있는 경우의 수를 구하는 문제
# 입력값 : 체스판의 가로는 abcdefgh 체스판의 세로는 12345678이라고 했을 때 가로세로의 위치를 입력
# 출력값 : 나이트가 움직일 수 있는 경우의 수

# n = input()

# 문제 해설
# 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     # if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#     if 1 <= next_row <= 8 and 1 <= next_column <= 8:
#         result += 1
#
# print(result)

# 3. 게임 개발
# 문제의 핵심
# 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발한다. 게임캐릭터가 있는 칸은 1 x 1 크기의 정사각형, 맵은 N x M 크기의 직사각형이다.
# 각 칸은 육지 또는 바다이다. 캐릭터는 상하좌우로 움직일 수 있고 육지에서만 움직일 수 있다. 캐릭터는 동서남북 중 한 곳을 바라본다.
# 캐릭터가 이동한 칸의 수를 구하는 문제이다.
# 입력 값
# 첫째 줄에 맵의 세로 크기(N) 가로 크기(M) 입력
# 둘째 줄에 캐릭터가 있는 좌표와 바라보는 방향 입력
# 셋째 줄에 각 칸이 바다인지 산인지 입력
# (단, 캐릭터의 처음 위치는 산이다.)

# 출력 값
# 캐릭터가 이동한 칸 수

# 문제 해설
# N, M을 공백으로 구분하여 입력 받기
# n, m = map(int, input().split())
#
# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0] * m for _ in range(n)]
# # 현재 캐릭터의 X 좌표, Y좌표, 방향을 입력받기
# x, y, direction = map(int, input().split())
# d[x][y] = 1  # 현재 좌표 방문 처리
#
# # 전체 맵 정보를 입력 받기
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# # 북, 동, 남, 서 뱡향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# # 왼쪽으로 회전
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
#
#
# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     # 왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 장면에 가보지 않은 칸이 없거나 바디인 경우
#     else:
#         turn_time += 1
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀 있는 경우
#         else:
#             break
#         turn_time = 0
#
# # 정답 출력
# print(count)
