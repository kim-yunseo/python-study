#1~100까지 합과 개수
# sum=0
# cnt=1
# while cnt<101:  #1~100까지 반복
#     sum+=cnt    #합을 누적
#     if cnt==100:
#         break
#     cnt+=1      #1씩증가
# print("개수는: ",cnt)
# print("합계는: ",sum)

sum=0
cnt=0
while cnt<100:  #1~100까지 반복
    cnt+=1      #1씩증가
    sum+=cnt    #합을 누적
    
print("개수는: ",cnt)
print("합계는: ",sum)