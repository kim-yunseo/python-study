#for i in range(6)
# =>0~5 6번 반복

snack={
    "새우깡":3000,
    "매운 새우깡":3500,
    "양파링":4000
}
for i in snack:
    print(i)             #키만 출력
for i in snack.items():  #전부 출력
    print(i)
for i in snack.values(): #값만 출력
    print(i)

fruit=["파인애플","참외","배","오렌지","골드키위"]
cart=[]
for i in fruit:
    if len(i)<=3:
        cart.append(i)
print(cart)