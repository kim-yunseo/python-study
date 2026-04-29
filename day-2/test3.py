pay=int (input("투입할 돈을 입력하세요: "))
mon=int (input("물건값을 입력하세요: "))
re=pay-mon
print(f"거스름돈: {re}")
coin500s = re//500
print(f"500원 동전의 개수: {coin500s}")
re=re%500
coin100s = re//100
print(f"100원 동전의 개수: {coin100s}")
