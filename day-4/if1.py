a=input("영어 한 글자를 입력하세요: ")
if  a.isupper():
    print(a.lower())
else:
    print(a.upper())

sc=int(input("점수를 입력하세요: "))
#if 81<=sc<=100:
#if sc>=81 and sc<=100: 
if (sc>=81) & (sc<=100):
    print("A")
elif (sc>=61) & (sc<=80):
    print("B")
elif (sc>=41) & (sc<=60):
    print("c")
elif (sc>=21) & (sc<=40):
    print("D")
else:
    print("E")