class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, val1, val2):
        return cls(val1 + val2)

number = FixedFloat(23.7654)
new_number =  FixedFloat.from_sum(4.555, 5.444)
print(new_number)

class Euro(FixedFloat):
    def __init__(self,amout):
        super().__init__(amout)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro { self.symbol}{self.amount:.2f}>"

money = Euro.from_sum(34.432,23.546)
print(money)