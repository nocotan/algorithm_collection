

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Dequeuing from an empty queue")

        x = self.s1[-1]
        self.s1.pop()

        return x
