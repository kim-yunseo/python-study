name=input("상품 이름을 입력하세요: ")
price=int (input("가격을 입력하세요: "))
quan=int (input("수량을 입력하세요: "))
totle=price*quan
#print(name+"의 총 금액은"+totle+"원입니다") total이 문자이기 때문에 오류
print(name,"의 총 금액은",totle,"원입니다")
print(name+"의 총 금액은"+str(totle)+"원입니다")
print(f"{name}의 총 금액은 {totle}원 입니다")
# 숫자->문자로 변환: str
# print 안에서 f는 f-string이고 포맷 문자열이다
# f"~ {변수} ~"로 쓴다
# 실수는 float만 있음(8byt)