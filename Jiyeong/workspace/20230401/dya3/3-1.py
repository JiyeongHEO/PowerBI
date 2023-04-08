'''

# [튜플 ()]
추가수정삭제 안됨, 정해진값, 장점: 메모리사용량,속도
c = 1,2,3,4,5    #(1,2,3,4,5) type: tuple
a= (1,)   aa = (1)         #가능
b= a+(4,)        #(1,4) 추가됨
b= aa+(4,)       #안됨(aa가 한개고 ','없어서 int임....)

# [딕트 {}]
kye: 문자열,숫자,튜플 됨
삭제 del
a[0]        #인덱싱 안됨

# [ Bool ]
b=[1,2,3]
bbbb = 3 in b       #True
print(bool())       #False 아무것도 없으면
print(bool(''))     #F
print(bool([]))     #F
print(bool('a'))    #True

# [ range 클라스 ]
print(range(5))     #range(0,5)

* random으로 1~10사이 5개 정수 저장
import random
lst =[]
for i in range(5):
    num = random.randint(1,10)
    lst.append(nu0m)

*구구단 가로로 나오게    #i,j위치변경, end='', 결과에 두자리 %2d 또는 탭\t
for ii in range(2,10):
    print('     %d단\t' %ii , end='' )
for j in range(1,10):
    print('enter')
    for i in range(2,10):
        print('%d * %d= %2d\t'  % (i, j, i * j), end='' )


'''

'''
# [연습]
1. 주사위 2개를 5번던져 숫자합(2~12)이 나오는 갯수 : list index == 합-2 또는 dict{}사용
import random
res = []        #{}
for i in range(11):
    res.append(0)       # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for tt in range(100):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    sum = first + second
    res[sum-2] += 1
print(res.__len__())
for rr in range(res.__len__()):
    print('%d가 %d회' %(rr+2, res[rr]))


2. for continue 
grade = [90,88,35,56,73,29,49,88,93,100]
for g in grade:
    if g <90:   # g>=90이면 continue필요없음
        continue
    else:
        idx = grade.index(g)
        print('%d 번쨰(%d점):합격' % (idx + 1, g))

  
'''

'''
# [모듈 & 패키지]
예:~~python311\Lib
*모듈: .py 
 내장함수: builtin함수 ( len(),sum(),max(),min() ), import함수(from statistics import mean만 가져온다),
 사용자정의함수: def,  return a,b  #print시 튜플로받음 
 

* import math
def calcuRound(r):
    ret1 = r**2*math.pi
    ret2 = r**2*3.14
    return ret1, ret2       #튜플 또는 2개변수로 받기

*return '%s는 %d살인 성인이다' %(name,age)   #됨

* def iPutManyNums(name, *num):    #열거형객체( 튜플 )로 받음
def iPutManyNums(name,   n1, *num):  # 첫번째와 나머지들 나옴 
iPutManyNums(name, 1,2,3,4,5,6,7,8,9)     

* def check소수():
    num = 2
    cnt=0
    while num<=100:
        chk = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:     #return False
                chk = False
                break

        if chk == True:
            cnt+=1
        num += 1
    

      
*패키지: 폴더
'''
