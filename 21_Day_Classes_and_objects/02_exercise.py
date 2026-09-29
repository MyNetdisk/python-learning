# 创建一个名为PersonAccount的类。它有firstname、lastname、incomes、expenses属性和添加收入、添加支出以及账户余额方法。

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description=""):
        """添加一笔收入"""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("收入金额必须是大于0的数字")
        self.incomes.append({"amount": amount, "description": description})

    def add_expense(self, amount, description=""):
        """添加一笔支出"""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("支出金额必须是大于0的数字")
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        """计算总收入"""
        return sum(item["amount"] for item in self.incomes)

    def total_expense(self):
        """计算总支出"""
        return sum(item["amount"] for item in self.expenses)

    def account_balance(self):
        """计算账户余额"""
        return self.total_income() - self.total_expense()


# 测试代码
account = PersonAccount('John', 'Doe')
account.add_income(100, "兼职")
account.add_expense(200, "购物")

print("账户余额:", account.account_balance())  # -100
print("总收入:", account.total_income())  # 100
print("总支出:", account.total_expense())  # 200
