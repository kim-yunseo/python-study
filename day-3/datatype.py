#리스트
subway=["아이유","변우석","박지훈","유재석"]
print(subway)
subway.append("장원영")       #추가
print(subway)
subway.insert(1,"카리나")     #삽입
print(subway)

print(subway.index("박지훈")) #위치 3

print(subway.pop())          #뒤 자료 삭제
print(subway)

name=subway.pop(1)           #삭제된 값 반환
print(name)

subway.remove("유재석")
print(subway)

subway.append("아이유")
print(subway)

print(subway.count("아이유"))

subway.remove("아이유")        #하나만 삭제
print(subway)

num_list=[2,4,5,1,3]
print(num_list)

num_list.sort()               #오름차순(작->큰)정렬
print(num_list)               

num_list.reverse()            #내림차순
print(num_list)               

num_list.clear()              #리스트 전체 삭제
print(num_list)

# 튜플: 순서가 있다, 나열형, 값 변경불가
menu=("김밥","오뎅")
print(menu)
#menu[1]="피자"                #오류 값 변경불가
#print(menu)

#언팩킹: 한번에 값을 넣는 거
(name, age, addr)=("이순신",30,"안산")
print(name,age,addr)

#딕셔너리: 키와 값이 쌍으로 구성
classroom={407:"개발자과정", 402:"영상과정"}
print(classroom)
print(classroom[407])          #대괄호
#print(classroom[404])         #오류

print(classroom.get(407))      #값 출력
print(classroom.get(404))      #Nome

print(classroom.keys())        #키만 출력
print(classroom.values())      #값만 출력
print(classroom.items())       #모두 출력

del classroom[402]             #del->다른 것도 삭제 가능
print(classroom)
