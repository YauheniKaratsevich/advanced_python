class Money:
    def __init__(self, value, currency="USD"):
        self.int_currency = "USD"
        self.rate = {"USD": 1, "BYN": 0.46, "EUR": 1.15, "CYN": 0.15}
        self.value = value
        self.currency = currency
        self.int_value = self.value * self.rate[self.currency]

    def __str__(self):
        return ("{} {}".format(self.value, self.currency))

    def __mul__(self, other):
        result_currency = self.currency
        result_value = self.value * other
        return Money(result_value, result_currency)

    def __rmul__(self, other):
        result_currency = self.currency
        result_value = self.value * other
        return Money(result_value, result_currency)

    def __add__(self, other):
        result_currency = self.int_currency
        result_value = self.int_value + other.int_value
        return Money(result_value, result_currency)

    def __radd__(self, other):
        result_currency = self.int_currency
        result_value = self.int_value + other
        return Money(result_value, result_currency)

    def change(self, cur1, cur2):
        return self.rate[cur1] / self.rate[cur2]

    def changeTo(self, cur):
        self.value = self.value * self.change(self.currency, cur)
        self.currency = cur


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(x)
    print(y)
    print(z)

    print(z + 3.11*x + y*0.8)
    print(z + 1*x + y*1)

    lst = [Money(10, "BYN"), Money(10), Money(12.01, "CYN")]
    s = sum(lst)
    print(s)
