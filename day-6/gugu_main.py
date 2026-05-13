import gugu_modul
a=True
while a:
    num=int(input("\n숫자를 선택하세요(1:세로 2:가로 0:종료): "))
    if num==1:
        gugu_modul.v_gugudan()
    elif num==2:
        gugu_modul.h_gugudan()
    elif num==0:
        a=False
    else:
        print("잘못 선택: 다시 입력")