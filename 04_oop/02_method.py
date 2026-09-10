"""
    메소드 : 클래스 내의 함수

    - 종류 -
    * 인스턴스 메소드
    * 클래스 메소드 (@classmethod)
    * 정적 메소드 (@staticmethod)
"""

class Account:
    bank_name = "KH 은행"
    MIN_DEPOSIT = 1000

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    # 인스턴스 메소드 : 객체의 데이터를 다룸. 첫번째 매개변수 self.
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # 클래스 메소드 : 클래스 자체를 다룸. 첫번째 매개변수 cls. @classmethod 지정
    @classmethod
    def from_dict(cls, data):
        """
            딕셔너리로부터 객체를 생성하는 메소드
        """
        return cls(data["owner"], data.get("balance", 0))

    # 정적 메소드 : 객체, 클래스와 무과한 기능을 담당하는 메소드(유틸리티)
    @staticmethod
    def is_valid_amount(amount):
        return amount >= Account.MIN_DEPOSIT

acc = Account("김종혁", 10000)
print(f"deposit --> {acc.deposit(3000)}")       # 인스턴스 메소드 호출

# 클래스 메소드 호출
acc2 = Account.from_dict({"owner": "김종혁", "balance": 10000})
print(f"owner: {acc2.owner}, balance: {acc2.balance}")

# 정적 메소드 호출
ㅈ