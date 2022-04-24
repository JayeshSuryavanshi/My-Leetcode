class ATM:
    def __init__(self):
        self.money = [0] * 5
        self.value = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, val in enumerate(banknotesCount):
            self.money[idx] += val

    def withdraw(self, amount: int) -> List[int]:
        withdraw = [0] * 5
        money = self.money.copy()
        for _ in range(4, -1, -1):
            if amount < self.value[_]: 
                continue
            balance = amount//self.value[_]
            if balance >= self.money[_]:
                withdraw[_] = self.money[_]
                self.money[_] = 0
            else:
                withdraw[_] = balance
                self.money[_] = self.money[_] - balance
                
            amount = amount - self.value[_] * withdraw[_]
            
        if amount == 0:
            return withdraw
        else:
            self.money = money
            return [-1]
                