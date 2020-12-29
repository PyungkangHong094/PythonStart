#문자열 슬라이싱 중요

# Section 04-2
# 문자여르 문자열연산, 슬라이싱

str1 = "I am Boy"
str2 = 'Nice man'
str3 = ''
str4 = str()
print(len(str1), len(str2), len(str3), len(str4))

escape_string = "Do you have a \"big collection\""
print(escape_string)
escape_strint2 = "Tab \t tat \t"
print(escape_strint2)

#Raw string
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

#멀티라인
multi = \
    """ 
    문자열 
    멀티라인 
    테스트"""
print(multi)
print('a'in str2)
print('z'not in str2)
print('f' in str2)

# 문자열 형 변환
print("==========문자열 형 변환==========")
print(str(77)+'a')
print(str(10.5))


a = 'niceman'
b = 'orange'

print(a.islower())
#끝글자가 무엇으로 끝나는지
print(a.endswith('n'))
print(a.capitalize())
print(a.replace('nice','good'))
print(list(reversed(b)))


c ='niceman'
d ='orange'

print(c[0:3])
print(c[:4])
print(c[:len(c)])
#3번째는 점프
print(d[0:4:2])
print(d[1:-2])
#문자열 슬라이싱
print(d[::-1])