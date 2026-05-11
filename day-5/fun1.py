#함수
# def add(a,b):
#     return a+b
# num1=int(input("첫번째 숫자를 입력하세요: "))
# num2=int(input("두번째 숫자를 입력하세요: "))
# sum=add(num1,num2)     #함수 호출, 리턴값 저장
# print(sum)

#sum():합계
#len():길이

def avg(score):
    if not score:
        return 0
    return sum(score)/len(score)
    
score_list=[100,80,20,50]
aver_res=avg(score_list)
print(aver_res)