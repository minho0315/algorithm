########### 기초-출력 ############
# # 001
# print("Hello")

# # 002
# print("Hello World")

# # 003
# print("Hello")
# print("World")

# # 004
# print("'Hello'")

# # 005
# print('"Hello World"')

# # 006
# print("\"!@#$%^&*()\'")

# # 007
# print('"C:\\Download\\\'hello\'.py"')

# # 008
# print("print(\"Hello\\nWorld\")")

######### 기초-입출력 ###########
# # 009
# c = input()
# print(c)

# # 010
# n = input()
# print(n)

# # 011
# f = input()
# print(f)

# # 012
# a = input()
# b = input()
# print(a)
# print(b)

# # 013
# a = input()
# b = input()
# print(b)
# print(a)

# # 014
# a = input()
# print(a)
# print(a)
# print(a)

# # 015
# a,b = input().split()
# print(a)
# print(b)

# # 016
# c1, c2 = input().split()
# print(c2, c1)

# # 017
# s = input()
# print(s,s,s)

# # 018
# a,b = input().split(':')
# print(a,b,sep=':')

# # 019
# y, m, d = input().split('.')
# print(d,m,y,sep='-')

# # 020
# a,b = input().split('-')
# print(a,b,sep='')

# # 021
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

# # 022
# s = input()
# print(s[0:2],s[2:4],s[4:6])

# # 023
# a,b,c = input().split(':')
# print(b)

# # 024
# w1, w2 = input().split()
# s = w1 + w2
# print(s)

######## 기초-값변환 ############
# # 025
# a,b = input().split()
# c= int(a) + int(b)
# print(c)

# # 026
# a = input()
# b = input()
# c = float(a) + float(b)
# print(c)

# # 027
# a = input()
# n = int(a)
# print('%x'%n)

# # 028
# a = input()
# n = int(a)
# print('%X'%n)

# # 029
# a = input()
# n = int(a,16)
# print('%o'%n)

# # 030
# n = ord(input()) #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
# print(n)

# # 031
# c = int(input())
# print(chr(c))

######### 기초-산술연산 ###########
# # 032
# n = int(input())
# print(-n)

# # 033
# n = ord(input())
# print(chr(n+1))

# # 034
# a,b = input().split()
# c = int(a) - int(b)
# print(c)

# # 035
# a, b = input().split()
# c = float(a) * float(b)
# print(c)

# # 036
# w,n = input().split()
# print(w*int(n))

# # 037
# n = input()
# s = input()
# print(int(n)*s)

# # 038
# a,b = input().split()
# c = int(a)**int(b)
# print(c)

# # 039
# a,b = input().split()
# c = float(a)**float(b)
# print(c)

# # 040
# a,b = input().split()
# print(int(a)//int(b))

# # 041
# a,b = input().split()
# print(int(a)%int(b))

############ 기초-값변환 ###########
# # 042
# f = float(input())
# print(round(f,2))

############# 기초-산술연산 ##########
# # 043
# f1,f2 = input().split()
# f3 = float(f1)/float(f2)
# print('%.3f'%f3)

# # 044
# a, b = input().split()
# c = int(a) + int(b)
# print(c)
# c = int(a) - int(b)
# print(c)
# c = int(a) * int(b)
# print(c)
# c = int(a) // int(b)
# print(c)
# c = int(a) % int(b)
# print(round(c,2))
# c = int(a) / int(b)
# print(round(c,2))

# # 045
# a,b,c = input().split()
# s = int(a) + int(b) + int(c)
# avg = s / 3
# print(s, round(avg,2))

######### 기초-비트시프트연산 ###########
# # 046
# #python에서 실수 값에 대한 시프트 연산은 허용되지 않고 오류가 발생한다.
# a = input()
# n = int(a)
# print(n<<1)

# # 047
# a, b = input().split()
# a1 = int(a)
# b1 = int(b)
# print(a1<<b1)

######## 기초-비교연산 ##############
# # 048
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a<b)

# # 049
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a == b)

# # 050
# a , b = input().split()
# a = int(a)
# b = int(b)
# print(a<=b)

# # 051
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a!=b)

############ 기초-논리연산 ##############
# # 052
# n = int(input())
# print(bool(n))

# # 053
# n = bool(int(input()))
# print(not n)

# # 054
# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))

# # 055
# a, b = input().split()
# print(bool(int(a)) or bool(int(b)))

# # 056
# a,b = input().split()
# c = bool(int(a))
# d = bool(int(b))
# print((c and (not d)) or ((not c) and d))

# # 057
# a, b = input().split()
# c = bool(int(a))
# d = bool(int(b))
# print((c and d)or ((not c) and (not d)))

# # 058
# a, b = input().split()
# c = bool(int(a))
# d = bool(int(b))
# print(not(c or d))

######### 기초-비트단위논리연산 ############
# # 059
# a = input()
# b = int(a)
# print(~b)

# # 060
# a,b = input().split()
# c = int(a)
# d = int(b)
# print(c&d)

# # 061
# a, b = input().split()
# c = int(a)
# d = int(b)
# print(c|d)

# # 062
# a, b = input().split()
# c = int(a)
# d = int(b)
# print(c^d)

# ####### 기초-3항연산 ##########
# # 063
# a, b = input().split()
# a = int(a)
# b = int(b)
# c = (a if (a>=b) else b)
# print(c)

# # 064
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = (a if a<b else b) if ((a if a<b else b)<c) else c
# print(d)

# ########## 기초-조건/선택실행구조 ###########
# # 065
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if(a%2==0):
#   print(a)
# if(b%2==0):
#   print(b)
# if(c%2==0):
#   print(c)

# # 066
# a, b, c = input().split()
# a = int(a)
# b= int(b)
# c = int(c)
# if(a%2==0):
#   print("even")
# else:
#   print("odd")
# if(b%2==0):
#   print("even")
# else:
#   print("odd")
# if(c%2==0):
#   print("even")
# else:
#   print("odd")

# # 067
# n = int(input())
# if n<0:
#   if n%2==0:
#     print('A')
#   else:
#     print('B')
# else:
#   if n%2==0:
#     print('C')
#   else:
#     print('D')

# # 068
# n = int(input())
# if n >=90:
#   print('A')
# elif n >=70:
#   print('B')
# elif n >=40:
#   print('C')
# else:
#   print('D')

# # 069
# s = input()
# if s=='A':
#   print("best!!!")
# elif s=='B':
#   print("good!!")
# elif s=='C':
#   print("run!")
# elif s=='D':
#   print("slowly~")
# else:
#   print("what?")

# # 070
# n = int(input())
# if n//3==1:
#   print("spring")
# elif n//3==2:
#   print("summer")
# elif n//3==3:
#   print("fall")
# else:
#   print("winter")