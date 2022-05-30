#FixedPoint Math Module
# by jmooremcc

__VERSION__ = 1.0

class FixedPoint:
    def __init__(self, value):
        if type(value) == float:
            self._value = int(value * 100)
        elif type(value) == int:
            self._value = value * 100
        elif type(value) == FixedPoint:
            self._value = value._value

    @property
    def value(self):
        return self._value / 100

    def __add__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self.value + other.value)
        else:
            return FixedPoint(self.value + other)

    def __iadd__(self, other):
        self._value = self.__add__(other)._value
        return self

    def __sub__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self.value - other.value)
        else:
            return FixedPoint(self._value - other)

    def __isub__(self, other):
        self._value = self.__sub__(other)._value
        return self

    def __mul__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self.value * other.value)
        else:
            return FixedPoint(self.value * other)

    def __imul__(self, other):
        self._value = self.__mul__(other)._value
        return self

    def __truediv__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self._value / other._value)
        else:
            return FixedPoint(self._value / other)

    def __itruediv__(self, other):
        self._value = self.__truediv__(other)._value
        return self

    def __eq__(self, other):
        if type(other) == FixedPoint:
            return self._value == other._value

    def __lt__(self, other):
        if type(other) == FixedPoint:
            return self._value < other._value

    def __gt__(self, other):
        if type(other) == FixedPoint:
            return self._value > other._value

    def __le__(self, other):
        if type(other) == FixedPoint:
            return self._value <= other._value

    def __ge__(self, other):
        if type(other) == FixedPoint:
            return self._value >= other._value

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.value}"



if __name__ == "__main__":
    price = FixedPoint(0.69)
    qty = FixedPoint(5)
    total = price * qty
    print(f"{total}  {type(total)}")

    total = qty * price
    print(total)

    sum = qty + price
    print(sum)

    qty += price
    print(qty)

    qty -= price
    print(qty)

    value = qty / FixedPoint(3)
    print(value)

    print(FixedPoint(0.1) + FixedPoint(0.1) + FixedPoint(0.1))

    print(f"{price=} {qty=}")
    print(f"{price == price=}")
    print(f"{price < price=}")
    print(f"{price > price=}")
    print(f"{price <= price=}")
    print(f"{price >= price=}")
    print(f"{price == qty=}")
    print(f"{price > qty=}")
    print(f"{price < qty=}")
    print(f"{price <= qty=}")
    print(f"{price >= qty=}")

    print("Finished...")