# input("출력문자") : 키보드로 입력, 기본적으로 문자로 입력받음
#정수로 입력하려면 괄호치고 앞에 int

n="apple"
print("i like",n)   #띄어쓰기가 됨
print("i like"+n)   #띄어쓰기가 안됨
print(3+5)          #8
print("결과는 "+20)  #오류
#print는 줄이 자동으로 바뀜
#+일 떄 문자는 연결, 숫자는 더하기, 문자+숫자는 안됨

#int 실습
a=int (input("첫번째 숫자를 입력하세요 "))
b=int (input("두번째 숫자를 입력하세요 "))
sum=a+b
print(sum)
name=input("이름을 입력하세요: ")
print(name)