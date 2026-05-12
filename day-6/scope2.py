# 스코프(scope)
#파이썬은 변수를 가까운 영역부터 찾는다
#LEGB 규칙(Local -> Enclosing -> Global -> Built-in)
#Enclosing: 바깥 함수 변수 
#Built-in: python이 기본 제공하는 이름(print,input,len...)
a = '홍길동'
b = 99

def function1():
    a = '이순신'       #Enclosing 변수
    c = [1 ,2 ,3]
    
    def function2():
        d = (1, 2, 3)
        print('Local a =',a)  #이순신
        print('Local b =',b)  #99
        print('Local c =',c)  #[1,2,3]
        print('Local d =',d)  #(1,2,3)
        print('-'*30)
        
    
    function2()
    print('Enclosing a =',a)  #이순신
    print('Enclosing b =',b)  #99
    print('Enclosing c =',c)  #[1,2,3]
#    print('Enclosing d =',d) #오류
    print('-'*30)
function1()
print('Global a =',a)         #홍길동
print('Global b =',b)         #99
#print('Global c =',c)        #오류
#print('Global d =',d)        #오류
print('-'*30)