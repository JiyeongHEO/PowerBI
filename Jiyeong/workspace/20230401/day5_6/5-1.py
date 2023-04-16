'''
#[예외처리]
try ~ except ~ finally ~

try:
    a=4
    b=0
    print(a/b)
except Exception as eee:
    print('오류정보: ', eee)
finally:
    print('끝')

'''


'''
#[file]

'''
# contents= ['이순신','남자','강북']
# fff = open('file2.txt','a')
# for i in range(len(contents)):
#     print(i)
#     fff.write('%s\n' %(contents[i]))
# fff.close()
#
#
# fff = open('file2.txt','r')
# while True:
#     ll =fff.readline()
#     if not ll:
#         break
#     print(ll, end=' ')
# fff.close()
#
#
# with open('score.scv','r') as f:
#     while True:
#         ll =f.readline()
#         if not ll:
#             break
#         print(ll, end=' ')
# f.close()



#===> 주피터로...
# anaconda3 환경변수 추가 (anaconda3, /Scripts. /Library/bin)

