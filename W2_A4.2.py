class MathSeries:
    # @staticmethod
    def factorial_recursive(self,n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * self.factorial_recursive(n - 1)


    # @staticmethod
    def fibonacci_recursive(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2))

    def fibonacci_series(self,n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        series = []
        for i in range(n):
            series.append(self.fibonacci_recursive(i))
        return series

if __name__ == "__main__":
    n = 5
    obj1= MathSeries()
    print("Factorial (recursive):", obj1.factorial_recursive(n))
    print("Fibonacci (recursive):", obj1.fibonacci_series(n))
