#재귀 호출(함수 내부에서 자기자신을 호출)
#5!(팩토리얼)
# def fact(n):
#     if n==1:
#         return 1             #2) 마지막에 fact(1)일때 1을 리턴
#     else:
#         return n * fact(n-1) #1) -1을 하고 곱함, 5*fact(4) 3) 2*1, 3*2 순서대로 대입

# a=int(input("정수를 입력하세요: "))
# res=fact(a) #함수 호출, 인수 a(정수) 보냄
# print(a,"!는",res,"입니다")

def sum(u):
    if u==1:
        return 1
    else:
        return u+sum(u-1)
b=int(input("정수를 입력하세요: "))
r=sum(b)
print(f"1부터 {b}까지의 합: {r}")