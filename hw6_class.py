class Money:
    def __init__(self, value, currency="USD"):
        self.rate = {"USD": 1, "BYN": 0.46, "EUR": 1.15, "CYN": 0.15}
        self.value = value
        self.currency = currency

    def __str__(self):
        return "{:.2f} {}".format(self.value, self.currency)

    def __mul__(self, other):
        return Money(self.value * other, self.currency)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if type(other) != type(self):
            return self
        if self.currency != other.currency:
            result_value = other.change(self.currency)
        else:
            result_value = other.value
        return Money(result_value + self.value, self.currency)

    def __radd__(self, other):
        return self.__add__(other)

    def change(self, cur):
        return self.value * self.rate[self.currency] / self.rate[cur]

    def changeTo(self, cur):
        self.value = self.change(cur)
        self.currency = cur


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")

    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "CYN")]
    s = sum(lst)
    print(s)
