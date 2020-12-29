# Section04-3
# 파이썬 데이터 타입 자료형
# 리스트, 튜플

#리스트(순서 , 중복 ,수정, 삭제)
# 선언

a = []
b = list()
c = [1,2,3,4]
d = [10,100,'pen','banana' ,'orange']
e = [10,100,['pen','banana' ,'orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100,1000,10000]
print(c)
c[1] = ['a','b','c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()
# 리스트 함수
y=[5,2,3,1,4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(2)
y.remove(7)
print(y)
y.pop()
print(y)
ex = [11,22]
# y.append(ex)
y.extend(ex)
print(y)

# 삭제 : del, remove, pop

# 튜플(순서, 중복을 허용 , 수정 안되고 , 삭제도 안된다 )

a = ()
b = (1,)
c = (1,2,3,4)
d = (10,100,('a','b','c'))

print(c[2])
print(c[3])
print(d[2][1])

print(c+d)
print()
print()
#튜플 함수
z =(5,2,1,3,4)
print(z)
print(3 in z )
# 자기가 찾고자 하는 것이다
print(z.index(2))
# 카운트
print(z.count(4))



