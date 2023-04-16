'''
# [모듈 & 패키지] - 2
...이어서
* 함수 - 재귀:
    # 5*4*3*2*1의 값
    def factorial(n):
        if n==1:
            return 1
        else:
            n* factorial(n-1)

*패키지: 폴더
'''

'''
#[파일 입출력]
생성 open(이름, mode)
    'w' - 없으면 생성됨, 있으면 기존거 삭제함(overwrite아님)
    'a' - append
    'r' - read only
끝 close() 
    # fff = open('0409.txt','w')
    # for i in range(1,11):
    #     fff.write('%d\n' %(i))
    # fff.close()

.write(i)               #안됨
.write('%d\n' %(i))     #됨

.readline()                             #한줄씩, 보통 while이용
        fff = open('0409.txt','r')      #mode변경 주의
        while True:
            ll =fff.readline()
            if not ll:                  # line없으면 끝
                break
            print(ll, end=' ')
            
.read()     #통채로읽음

'''

# fff = open('0409.txt','w')
# for i in range(1,11):
#     fff.write('%d\n' %(i))
# fff.close()

# fff = open('0409.txt','a')
# for i in range(11,21):
#     fff.write('%d\n' %(i))
# fff.close()


# fff = open('0409.txt','r')
# while True:
#     ll =fff.readline()
#     if not ll:
#         break
#     print(ll, end=' ')
# fff.close()

# fff = open('0409.txt','r')
# print(fff.read())
# fff.close()


'''
# [클라스 객체]
함수 ->(여러개 -> '메소드'가 됨)+ 속성-> 클라스: 설계도 -> 객체: 결과물
    # class calc:
    #     def add(self, first, second):         #변수저장안하고 바로~ (메소드   호출시마다)
    #         print(first  + second)
    # ccc = calc()
    # ccc.add(2,3)
    
    class Person:
    def per(self, n, a):        #번수 self로 저장함 -> 다른함수에서 실행
        self.name = n           #번수 self로 저장함 -> 다른함수에서 실행
        self.age = a            #번수 self로 저장함 -> 다른함수에서 실행
    def intro(self):
        print(self.name, self.age)

    hong = Person()
    hong.per('홍길동',10)
    hong.checkAge()

'''


'''
# [상속]
class Parent:
    def money(self):
        print("부모 돈")

class Child(Parent):        #상속받음
    pass                    #아무내용 없을때

ch = Child()               
ch.money()

# class Parent:
#     def work(self):
#         print()
# class Children(Parent):
#     def study(self):
#         print("children 스터디")
# class Girl(Children):
#     def study(self):
#         print("girl 스터디")           #메소드 재정의
# 
# g1=Girl()
# g1.study()



# [생성자 ] 초기화 메소드
class Employee:
    pay=0
    def __init__(self, type, name):
        if type=='P':
            self.type = '정규직'
        else:
            self.type = '계약직'
        self.name = name

class Temp(Employee):
    def __init__(self, type, name,    wh, hourly):
        super().__init__(type, name)        #부모 생성자를 상속 받아 씀
        self.wh = wh
        self.hourly = hourly
        self.pay = self.wh * self.hourly

type1 = input('고용형태?? ')
..생략..
elif type1 == 'T':
    name = '홍길동'
    wh = 5
    hourly = 10000
    worker2 = Temp(type1, name, wh, hourly)     #여기서 쓸거면 바로 worker2.name해도 됨
    print('고용형태:%s 이름:%s 급여:%d' % (worker2.type, worker2.name, worker2.pay))  #3자리끊기: format(값, 3,d)

'''



'''
#[모듈] .py 파일들
module.py로...
* import time
* from re import findall         #findall(찾는것, 전체문장)
    findall([0-9]{3}, str1))     #['123', '555']
    [a-z|A-Z]                    #대소상관이 문자찾기
    [가-힣]                       #한글전체    
  from re import match           #match()     
*
*

'''


from re import findall,match
from statistics import mean

emp=['2023김가을100','2023이가을이200','2023박가을300'] #입사년도,이름,급여
pay=[]

#급여평균 by 함수로
def pay_pro(xxx):
    for str in emp:
        #name = findall('[가-힣]{3}', str)
        p=findall('[0-9]{3}$', str)             #type: list
        pp = int(p[0])
        pay.append(pp)
    #print(mean(pay))
    return mean(pay)

meanpay = pay_pro(emp)

#급여평균이상 by 함수로
for i in range(len(emp)):                       #idx로 돌림
    if pay[i] >= meanpay:
        print(pay[i],',',emp[i])


        
    