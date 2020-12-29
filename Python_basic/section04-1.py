# 파이썬 데이터 타입 종류
# Boolean - 0 
# Numbers 
# String
# Bytes

# 집합 자료형 
# Lists
# Tuples
# Sets
# Dictionaries 


#데이터 타입 

v_str1 = 'Niceman'
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Hong", 
    "age" : "27",
    "gender" : "Male"
}
v_list = [3,5,7]
v_tuple = 3, 5, 7
v_set = {7,8,9}
print("--------Print Type----------")
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))
print("---------------------------")
print("")
i_1 = 39
i_2 = 909
big_int1 = 1000000000000000000
bit_int2 = 9999999999999999999
f_1 = 1.234
f_2 = 3.756
f_3 = .5
f_4 = 10.

print("-------숫자형 프린트-------")
print(i_1* i_2)
print(big_int1 * bit_int2)
print(f_1 ** f_2)
print(f_3 + f_4)
print("---------------------------")

a = 5.
b = 4

# 형변환
# int, float, complex
print(type(a), type(b))
res = a + b
print("Print type:",type(res))
print(int(res))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

#단한 연산자
y = 100
y += 100

#수치 연산 함수 

# 수치 연산 함수
print(abs(-7))
print(abs(-6))
n, m = divmod(100,8)
print("몫:",n,"나머지:", m)

x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3))
print("------math------")

import math
#ceil
print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수
print(math.ceil(8.999))

#floor
print(math.floor(3.874)) # x 이하의 수 중에서 가장 큰 정수
print(math.floor(-25.5))

#pi
print(math.pi)

# 그 밖에 함수는 아래 URL 참조
# https://docs.python.org/3/library/math.html

# 2진수 변환
print(bin(50)) #0b로 시작