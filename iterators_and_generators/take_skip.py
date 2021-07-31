class take_skip:
    def __init__(self, step, count):
        self.count = count
        self.step = step
        self.produced = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.produced < self.count:
            produced_so_far = self.produced
            self.produced += 1
            return self.step * produced_so_far
        else:
            raise StopIteration()

# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)