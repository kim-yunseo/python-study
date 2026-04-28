import turtle      #모듈 이용

t=turtle.Turtle()  #turtle 객체 생성, t 변수에 할당
t.shape("turtle")  #모양설정

radius = 50        #반지름
t.circle(radius)   #반지름이 radius인 원을 그림
t.fd(30)           #앞으로 이동
t.circle(radius)
t.fd(30)
t.circle(radius)
t.fd(50)
for _ in range(4): #반복문
    t.forward(2*radius)
    t.right(90)    #오른쪽으로 이동
#한 변의 길이가 반지름*2인 정사각형을 그림
#for 문안에서 for 뒤 변수를 사용하지 않으면 그냥 _을 쓴다
for _ in range(3):
    t.forward(2*radius)
    t.right(120)