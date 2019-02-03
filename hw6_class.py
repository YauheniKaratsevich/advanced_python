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

    def __iadd__(self, other):
        self.int_value += other.int_value
        self.value += other.int_value / self.currency


if __name__ == "__main__":
    a = Money(10, "BYN")
    b = Money(100, "CYN")
    c = Money(10, "USD")
    print(a, b, c)

    print(a + 3.11 * b + c * 0.8)

    z = [Money(10, "BYN"), Money(10, "USD"), Money(10, "CYN")]
    r = sum(z)
    print(r)
