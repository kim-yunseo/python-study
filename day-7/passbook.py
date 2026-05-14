class Passbook:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,money):
        self.balance+=money
        print(f"입금 금액: {money}")
        print(f"현재 잔액: {self.balance}")
        print('-'*30)

    def withdraw(self,money):
        if self.balance<money:
            print("잔액 부족")
            print('-'*30)
        else:
            self.balance-=money
            print(f"출금 금액: {money}")
            print(f"현재 잔액: {self.balance}")
            print('-'*30)

    def showInfo(self):
        print(f"예금주: {self.owner}")
        print(f"현재 잔액: {self.balance}")
        print('-'*30)


class MinusPassbook(Passbook):
    def withdraw(self,money):
        result=self.balance-money
        if result<-1000000:
            print("마이너스 한도 초과")
            print('-'*30)
        else:
            self.balance-=money
            print(f"출금 금액: {money}")
            print(f"현재 잔액: {self.balance}")
            print('-'*30)

account1=Passbook("홍길동",100000)
account1.showInfo()
account1.deposit(50000)
account1.withdraw(120000)
account1.withdraw(70000)

account2=MinusPassbook("김철수",100000)
account2.showInfo()
account2.withdraw(120000)
account2.withdraw(9000000)
