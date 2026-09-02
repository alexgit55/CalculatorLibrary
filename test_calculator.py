import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(1, 2) == 3
        assert calculator.add(-3, 5) == 2
        assert calculator.add(0, 0) == (
            0
        )

    def test_subtraction(self):
        assert calculator.subtract(10, 5) == 5
        assert calculator.subtract(-3, 5) == -8
        assert calculator.subtract(0, 0) == 0

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 5 == calculator.division(10, 2)