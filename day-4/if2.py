# num=input("주민번호를 입력하세요: ")
# if num[7]=='1' or num[7]=='3':
#     print("남자입니다")
# else:
#     print("여자입니다")

# numl=num.split('-')[1]
# if numl[0]=='1' or numl[0]=='3':
#     print("남자입니다")
# else:
#     print("여자입니다")

# numl=num.split('-')
# if numl[1][0] =='1' or numl[1][0] =='3':
#     print("남자입니다")
# else:
#     print("여자입니다")

a=int(input("첫번째 숫자를 입력하세요: "))
b=int(input("두번째 숫자를 입력하세요: "))
c=int(input("세번째 숫자를 입력하세요: "))

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)