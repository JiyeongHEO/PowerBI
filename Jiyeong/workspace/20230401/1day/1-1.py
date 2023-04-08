#한줄주석

'''
여러줄
'''

'''
var1=10
var2='hello'
print(var1)
print(var2)
print(id(var1)) #주소값
var3=10
print(id(var3)) #var1과 같다
'''

''' 
a=10
print(a)
a=10.5
b=a
print(id(a)) #같
print(id(b)) #다
b= int(a) #소수점버리기  float(a): 소수점살리기
'''

'''
print(True)  #False 
a=True
print(int(a))  #1
'''

'''
숫자 + 문자 = err
int(문자) = 문자->숫자 가능
type(a) # <class 'int'> 그외 float, bool, str....
10*2, 10**2:제곱
'''

'''
[연산자]
+)산술:
//:몫,  %:나머지
float % float  = 나머지00004가 됨(반올림하면 잘못됨) -> float*10 % float*10 = 나머지*10

+)논리: and, or, not

+)대입: a,b=100,200됨, (a,b):교환 , 패킹(*):
    lst1 = 1,2,3,4,5 #튜플
    list2=[1,2,3,4,5] #리스트
    v1,v2 = lst1 #err
    v1,*v2 = lst1 #리스트화    1 [2,3,4,5] 
    v1,*v2, v3 = lst1 #리스트화   1 [2,3,4] 5
    print(v1, v2)
'''


'''
[표준입력]
num = input('숫자입력: ') #초록글자 # 'str'

num2 = int(input('숫자입력: ')) # int
'''
''' 
연습문제
1. su = 5
dan = 800
금액= su*dan
print('su 주소: ', id(su) )
print('dan 주소: ', id(dan))
print('금액: ', 금액)

2.
x=float(int(input('숫자입력: ')))
y = (2.5* (x**2)) + (3.3*x) + 6
print('2차방정식결과: ', y)

fat = int(input(' 지방입력: '))
calb = int(input(' 탄수입력: '))
prot = int(input(' 단백질입력: '))
tot = fat*9 + calb*4 + prot*4
print('-> 총칼로리: ', tot , 'Kcal')
'''

'''
[출력장치]
print(어쩌구 sep='-') #010-1111-2222

print(end='') print() #개행안함,  end='-' #위와같음 

format(변수, '.3f') #실수 && .3자리까지 표시한다(반올림됨)  '8.3f': 총 8자리로 우측정렬
'10d': 10진수 
print('10진수: %d' %a) #참조,10진수  %o:8진수  %x:16진수
print('10진수: %d, 8진수: %o 16진수~' %(a a a))

print('%d%%' %a) # %:escpae

+) 외부상수
print('이름: %s, 나이: %d' %(name, age))
print('이름: {} 나이:{}'.format(name, age))
'''

'''
[문자열]
\ escpae
[0:4]: 0포함 +4
[1:5:2]: 1부터 5자리, 2칸에한개씩
[0::3]: 3의배수

' '.join(리스트): 리스트[] 안의 것을 ' '(구분자)로 연결

print('현재온도는 %.1f입니다' %temp) #24.5(000000제거)
string.find('뭐') #index, int

# wwww = '20230401sunny'
# year = wwww[0:4]
# mon = wwww[4:6]
# day= wwww[6:8]
# weather = wwww[8:]
# txt = "%s년 %s월 %s일 날씨:%s"
# print(txt %(year,mon,day,weather))

# word1=input('첫번쨰: ')
# word2=input('두번쨰:')
# word3=input('세번쨰:')
# sum = word1[0]+word2[0]+word3[0]
# print(' 1:%s \n 2:%s \n 3:%s ' %(word1,word2,word3) )
# print('=' * 20)
# print(' 약자:' , sum )

# sec = int(input('초 입력: '))
# min = int(sec/60)
# sec2 = int(sec%60)
# print('%d초는 %d분 %d초이다' %(sec, min, sec2))


# mymoney = int(input('가지고잇는돈: '))
# candy = int(input('사고싶은 캔디수: '))
# price = candy*200
# if price <= mymoney : 
#     changes = mymoney - price
#     print(changes)
# else :
#     print('너무많이삼')
'''

mymoney = 1000
coffee = 300
buy = int(input(' 몇개삼? 3개까지가능 if문없음..: '))
changes = mymoney - coffee*buy


coin1 = changes//500
changes2 = changes%500
coin2 = changes2//100

print(' 거스름돈 500원:%d개, 100원:%d개' %(coin1, coin2))
