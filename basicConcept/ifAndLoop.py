# ################## 조건문
# x = 15

# if x >= 15:
#   print(x)

# score = 85

# if score >= 90:
#   print("학점: A")
# elif score >= 80:
#   print("학점: B")
# elif score >= 70:
#   print("학점: C")
# else:
#   print("학점: F")

# score = 85

# if score >= 80:
#   pass # 나중에 작성할 코드
# else:
#   print('성적이 80점 미만입니다.')

# print('프로그램을 종료합니다')

# score = 85

# if score < 80: result = "Success"
# else: result = "Fail"

# print(score)

# score = 85
# result = "Success" if score > 80 else "Fail"

# print(score)

# a = [1,2,3,4,5,5,5]
# remove_set = {3,5}

# result=[]
# for i in a:
#   if i not in remove_set:
#     result.append(i)
# print(result)

# result=[i for i in a if i not in remove_set]
# print(result)

################ 반복문
# # while
# i = 1
# result = 0

# while i <= 9:
#   result += i
#   i += 1

# print(result)

# i = 1
# result = 0

# while i <= 9:
#   if i % 2 == 1:
#     result += i
#   i += 1

# print(result)

# # for문
# result = 0

# for i in range(1,10):
#   result += i

# print(result)


# scores = [90, 85, 77, 65, 97]

# for i in range(5):
#   if scores[i] >= 80:
#     print(i+1, "번 학생은 합격입니다.")

# scores = [90, 85, 77, 65, 97]
# cheating_list = {2,4}

# for i in range(5):
#   if i+1 in cheating_list:
#     continue
#   if scores[i] >= 80:
#     print(i+1, "번 학생은 합격입니다.")

# for i in range(2,10):
#   for j in range(1,10):
#     print(i, "X", "=", i*j)
#   print()