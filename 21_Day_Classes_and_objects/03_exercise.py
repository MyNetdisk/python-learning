class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, *args, **kwargs):
        """
        添加收入
        *args: 多个收入金额，例如 100, 200
        **kwargs: 可选备注信息，例如 note="工资"
        """
        for amount in args:
            if isinstance(amount, (int, float)) and amount > 0:
                self.incomes.append({"amount": amount, "info": kwargs})
            else:
                print(f"无效收入金额：{amount}")

    def add_expense(self, *args, **kwargs):
        """
        添加支出
        *args: 多个支出金额，例如 50, 30
        **kwargs: 可选备注信息，例如 note="餐饮"
        """
        for amount in args:
            if isinstance(amount, (int, float)) and amount > 0:
                self.expenses.append({"amount": amount, "info": kwargs})
            else:
                print(f"无效支出金额：{amount}")

    def total_income(self):
        return sum(item["amount"] for item in self.incomes)

    def total_expense(self):
        return sum(item["amount"] for item in self.expenses)

    def net_income(self):
        """计算净收入"""
        return self.total_income() - self.total_expense()

    def describe(self):
        print(f"姓名：{self.firstname} {self.lastname}")
        print(f"总收入：{self.total_income()}")
        print(f"总支出：{self.total_expense()}")
        print(f"净收入：{self.net_income()}")


# 测试代码
account = PersonAccount("John", "Doe")

account.add_income(5000, 200, note="工资和兼职")
account.add_expense(1500, 300, 100, note="房租、餐饮、交通")

account.describe()
