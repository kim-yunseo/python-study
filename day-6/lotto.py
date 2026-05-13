import random
def get_lotto():
    numbers=[]                  #0부터 시작
    while len(numbers)<6:
        n=random.randint(1,45)  #무작위 수, 1~45 사이
        if n not in numbers:    #중복 방지
            numbers.append(n)   #추가
    return numbers
    
print(f"로또번호는 {get_lotto()}입니다")
#get_lotto() 함수 호출