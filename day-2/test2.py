a=2000
cr=3000
cp=3500
anum=int (input("아메리카노 잔 수를 입력하세요: "))
crnum=int (input("카페라떼 잔 수를 입력하세요: "))
cpnum=int (input("카푸치노 잔 수를 입력하세요: "))
print(f"아메리카노 판매 개수: {anum}")
print(f"카페라떼 판매 개수: {crnum}")
print(f"카푸치노 판매 개수: {cpnum}")
sales=anum*a
sales=sales+crnum*cr
sales=sales+cpnum*cp
print(f"총 매출은 {sales}입니다")