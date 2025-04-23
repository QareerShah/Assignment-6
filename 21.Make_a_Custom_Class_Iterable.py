class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # returning self as iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # jab 0 se niche jaye, stop kar do
        value = self.current
        self.current -= 1
        return value

# 💡 Usage example
for number in Countdown(5):
    print(number)
