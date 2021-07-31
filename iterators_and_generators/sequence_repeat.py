class sequence_repeat:
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx < self.count:
            idx = self.current_idx
            self.current_idx += 1
            return self.sequence[idx % len(self.sequence)]
        else:
            raise StopIteration()

#
# result = sequence_repeat("abc", 5)
# for item in result:
#     print(item, end ="")
