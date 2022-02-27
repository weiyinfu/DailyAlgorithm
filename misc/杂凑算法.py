import numpy as np


class Hasher:
    def __init__(self):
        self.x = np.random.RandomState(0)
        self.a = self.x.randint(-128, 127, 128, dtype=np.int8)

    def update(self, x: bytes):
        for i in x:
            self.a[self.x.randint(0, len(self.a))] ^= (i + self.x.randint(0, 256))

    def get(self):
        return self.a.tobytes()


x = Hasher()
x.update(bytes("asdfasdf", 'utf8'))
ans = x.get()
print(ans, len(ans))
