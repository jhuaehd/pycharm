class CallCenter:
    def __init__(self):
        self.customers = []

    def is_empty(self):
        return self.customers == []

    def add(self, x):
        self.customers.insert(0, x)

    def next(self):
        return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)
# your code goes here
time = 0
while True:
    if c.is_empty():
        break
    for value in c.customers:
        if value == 'general':
            time = time * 5
            time = time + time
    print(time)
    break
c.next()