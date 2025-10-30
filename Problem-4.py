class MultipleCounter:
    def __init__(self, n):
        self.numbers = n

    def count_multiples(self):
        result = {}
        for i in range(1, 10):  
            count = 0
            for num in self.numbers:
                if num % i == 0:
                    count += 1
            result[i] = count
        return result



n = list(map(int, input("Enter numbers separated by spaces: ").split()))
counter = MultipleCounter(n)
print(counter.count_multiples())
