#내장함수
res=divmod(11,3)
print(res)               #3, 2 몫(//), 나머지(%)
print(abs(-5))           #abs: 절대값
print(pow(4,2))          #제곱, =4**2
print(max(10,30,5))      #()중에 최대값
print(min(10,30,5))      #()중에 최소값
print(round(23.89))      #반올림

import math              #math를 써야함
#from math import *      #math 모든 함수를 네임스페이스로 가져옴, math 안씀
#외장함수
print(math.floor(24.9))   #버림
print(math.ceil(24.1))    #올림
print(math.sqrt(16))      #제곱근(root)
print(math.factorial(5))  #팩토리얼
print(math.pi)            #원주율