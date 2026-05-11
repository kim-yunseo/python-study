# num1= int(input("짝수를 입력하세요: "))
# num2= int(input("홀수를 입력하세요: "))
# match num1%2, num2%2:
#     case 0,1:
#         print("num1은 짝수 num2는 홀수")
#     case 0,_:
#         print("num1은 짝수 num2는 아무숫자")
#     case _,1:
#         print("num1는 아무숫자 num2은 홀수 ")
#     case _:
#         print("둘다 오류")


num1= int(input("5의 배수를 입력하세요: "))
num2= int(input("3의 배수를 입력하세요: "))
match num1%5, num2%3:
    case 0,0:
        print("num1은 5의 배수 num2는 3의 배수") #break필요 없음
    case 0,_:
        print("num1은 5의 배수 num2는 아무숫자")
    case _,0:
        print("num1는 아무숫자 num2은 3의 배수 ")
    case _:
        print("둘다 오류")