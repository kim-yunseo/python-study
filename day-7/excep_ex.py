try:                         #수행 문장
    num=int(input("숫자를 입력하세요"))
    res= 10/num
except ValueError:           #예외 발생시 처리, 값 오류
    print("숫자가 아닙니다")
except ZeroDivisionError:    #0
    print("0으로 나눌 수 없습니다")
except Exception as e:       #나머지 모든 오류
    print("에러메시지:",e)
else:                        #정상적인 경우
    print(f"결과: {res}")
finally:                     #무조건 실행
    print("종료")