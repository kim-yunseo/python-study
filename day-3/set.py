# set(집합)
# 순서가 없음, 중복 불가
# {}, set([])

my_set={"홍길동","김길동","장길동"}
print(my_set)

football={"홍길동","김길동","장길동"}
baseball=set(["홍길동","오길동","김하성"])

print("----------교집합-----------")
print(football & baseball)               #교집합
print(football.intersection(baseball))   #교집합
print("----------합집합-----------")
print(football | baseball)               #합집합
print(football.union(baseball))          #합집합
print("----------차집합-----------")
print(football - baseball)               #차집합
print(football.difference(baseball))     #차집합
print("--------------------------")

#add 추가
football.add("김길동")                    #중복 불가 추가 안됨
print(football)

baseball.remove("오길동")                 #삭제
print(baseball)

print(type(baseball))                    #set

spo1=list(baseball)
print(type(spo1))                        #list

spo2=tuple(baseball)
print(type(spo2))                        #tuple