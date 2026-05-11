# a=True
# while a:
#     num=int(input("숫자를 입력하세요: "))
#     print(num)
#     if num==0:
#         a=False
# print("반복문 종료")

menu=["쫄면", "김밥", "냉면", "오뎅"]
b=input("메뉴 선택: ")
while b in menu:            # 조건이 참일때 수행, in은 포함 여부
    print(b)
    b=input("메뉴 선택: ")