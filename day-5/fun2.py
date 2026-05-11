#디폴트 인수: 함수의 매개변수가 기본값을 갖고 있을 수 있음
def greet(name,msg="별일없지"):
    print("안녕 "+name+" "+msg)

greet("홍길동")

##################################
def print_star(n=1):
    print("n= ",n)
    for i in range(n):
        print("*****")
print_star()     #인수 없음 1번 출력
print()
print_star(3)    #인수 있음 3번 출력