'''
[조건문]
# grad = int(input('점수 입력: '))
# if grad>=85:
#     print('우수')
# elif grad>=70:
#     print('보통')
# else:
#     print('저조')

# if h>=160 and age>=15:
#     print('탈수있다')

# age = int(input('나이?'))
# if age>7 and age<=19:
#     fare = 800
#     print('승차요금: %d원 이다' % (fare))
# else :
#     print('승차요금: 무료이다')

# if age==1:
#     pass
# else:
#     print('1아님')

*삼항연산
#result = num*2 if num>=5 else num+2  #5이상일때 *2 (아니면 +2)
'''

'''
[반복문]
# while num<=100:
#     if num%3==0:
#         print(num)
#     num+=1

*무한반복 break, 
# while True:
#     num = int(input('숫자???'))
#     if num!=0:
#         print('0이아님...')
#     else:
#         break

*홀수만 출력 continue
# while num<10:
#     num+=1
#     if num%2==0:
#         continue
#     print(num)
'''

'''
# [random]모듈 - import필요
.randint(a,b) a~b범위에서...
.random()

*주사위게임
# import random
# while True:
#     mm = int(input('숫자??'))
#     pp = random.randint(1,6)
#     print('(pp값:', pp,')')
#     if mm ==0:
#         print('종료합니다')
#         break
#     elif mm>pp:
#         print('내가이김 -끝')
#         break
#     elif mm==pp:
#         print('무승부')
#     else:
#         print('컴 이김')

*별그리기
# cnt = 1
# sss = '*'
# while cnt<6:
#     print(sss*cnt)
#     cnt+=1

# elif ww<=20:
#     aditional = (ww-10)*1000
#     print('%d원 추가부과' %(aditional))
# elif ww<=30:
#     aditional = 10*1000 + (ww-20)*2000
#     print('%d원 추가부과' % (aditional))
# elif ww<=40:
#     aditional = 10*1000+ 10*2000 + (ww-40)*3000
#     print('%d원 추가부과' % (aditional))

*이자
# init = 1000
# target = 2000
# y = 1
# while target > init :
#     init += init*0.08
#     print('%d년후 %d원..' % (y, init))
#     y+=1

'''
'''
[for문]
열거형객체: list[], str 

# for i in [1,2,3,4,5]:
#     print(i, end=' ')

# num = [1,2,3,[6,7,[10,11,12],8,9],4,5]
# num[3]                   #[6,7,[10,11,12],8,9]
# print(num[3][2][:2])     #10,11
# print(num[3][-2:])       #8,9

# a=[1,2,3]
# b=[4,5,6]
# a+b #[1,2,3,4,5,6]

*길이: len()
삭제 del a[인덱스]
뒤에추가 .append(요소):  b.append(b) #[1, [...]] 나자신 append
정렬 .sort(), sort(reverse=True)#내림차순 
정렬없이 .reverse() 
삽입 .insert(인덱스, 값)
삭제2 .remove(값)
'''
