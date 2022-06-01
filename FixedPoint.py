#FixedPoint Math Module
# by jmooremcc


__VERSION__ = 1.3
"""
FixedPoint Module
Performs fixed point arithmetic suitable for Currency operations
Examples:
    qty = FixedPoint(5)
    price = FixedPoint(0.69)
    total = qty * price
    
Change Log
    Version 1.0:
        Initial version
        
    Version 1.1:
        Streamlined operations to perform math operations using internal integer representation
        Minor bug fixes
        
    Version 1.2:
        Refined math operations to eliminate unnecessary multiplication or division
        added the ability to perform math operations in any order.
        Also added Fractions and other methods that allow the module to work with sum and mean functions
        when FixedPoint objects are used in a list
    
    Version 1.3:
        More refinements to support statistical ops with lists.
        Fixed bug that involved a mixed type liat including FixedPoints
"""

class FixedPoint(float):
    def __new__(cls, value, FPV=False):
        return super().__new__(cls, value)

    def __init__(self, value, FPV=False):
        if FPV:
            self._value = int((value*100)/100)
        elif type(value) == float:
            self._value = int(value * 100)
        elif type(value) == int:
            self._value = value * 100
        elif type(value) == FixedPoint:
            self._value = value._value
        else:
            self._value = int(value * 100)


    @property
    def value(self):
        return self._value / 100

    @value.setter
    def value(self, val):
        self._value = val

    def __add__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self._value + other._value, True)
        else:
            return FixedPoint(self.value + other)

    def __iadd__(self, other):
        self.value = (self.__add__(other))._value
        return self

    def __sub__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self._value - other._value, True)
        else:
            return FixedPoint(self.value - other)

    def __isub__(self, other):
        self.value = (self.__sub__(other))._value
        return self

    def __mul__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self._value * other.value, True)
        else:
            return FixedPoint(self.value * other)

    def __imul__(self, other):
        self.value = (self.__mul__(other))._value
        return self

    def __truediv__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self._value / other._value)
        else:
            return FixedPoint(self.value / other)

    def __itruediv__(self, other):
        self.value = (self.__truediv__(other))._value
        return self

    def __floordiv__(self, other):
        if type(other) == FixedPoint:
            return FixedPoint(self._value // other._value)
        else:
            return FixedPoint(self.value // other)

    def __ifloordiv__(self, other):
        self.value = (self.__floordiv__(other))._value
        return self

    def __radd__(self, other):
        return self.value + other

    def __rsub__(self, other):
        return self.value - other

    def __rmul__(self, other):
        return self.value * other

    def __rdiv__(self, other):
        return self.value / other

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

    def __cmp__(self, other):
        return int(self.value - other)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value:0.2f})"

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return self.value

    def __coerce__(self, other):
        return (int(self.value), int(other))


if __name__ == "__main__":
    price = FixedPoint(0.69)
    qty = FixedPoint(5)
    total = price * qty
    print(f"{total}  {type(total)}")

    total = qty * price
    print(f"{total=}")

    sum = qty + price
    print(f"{sum=}")

    qty *= qty
    print(f"{qty=}")

    qty += price
    print(f"{qty=}")

    qty -= price
    print(f"{qty=}")

    value = qty / FixedPoint(3)
    print(f"{value=}")

    qty /= FixedPoint(2)
    print(f"{qty=}")

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