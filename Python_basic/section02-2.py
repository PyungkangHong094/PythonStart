# Section 02 -2 
# python basic
# WarmUp coding 

# import this
import sys

#파이썬 기본 인코딩
#입력과 출력은 UTF-8이다
print(sys.stdin.encoding)
print(sys.stdout.encoding)


#변수 선언
# 그릇에 담는다고 생각하면 된다
myName = 'PK'

#조건문
if myName == "PK":
    print("Hi Pyungkang")

#반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)

#함수선언
def function():
    print("LINE here FUCNITON")
#함수 실행
function()

#클래스
class Cookie:
    pass

#객체 생성
#클래스에 정보값들을 출력해보자!
cookie = Cookie()

print(id(cookie))
print(dir(cookie))