class Board:
    def set_data(self, title, writer):
        self.title=title        #오른쪽은 호출 할 떄 받아온 매개변수 값 왼쪽은 객체
        self.writer=writer      #self 객체를 의미
        self.cnt=0
    
    def cntup(self):            #조회수를 구하는 함수
        self.cnt +=1            #매개변수가 없어도 self를 써야함

#게시판 객체 생성
board1 = Board()                #객체 변수=클래스(매개변수)
board2 = Board()

#클래스 함수 호출
board1.set_data("자바의 정석","홍길동")
board2.set_data("파이썬의 정석","오길동")

board1.cntup()
board1.cntup()
board2.cntup()
print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)

#board3=Board()
#board3=cntup() 오류 set_data를 호출하지 않아서 cnt가 생성이 안됨