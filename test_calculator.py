import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(1, 2) == 3

    def test_subtraction(self):
        assert calculator.subtract(5, 3) == 2
