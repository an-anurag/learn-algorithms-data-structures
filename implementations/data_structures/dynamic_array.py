import ctypes


class DynamicArray:

    def __init__(self):
        self.n = 1
        self.capacity = 1
        self.A = self._create_array(self.capacity)

    def __len__(self):
        return len(self.A)

    def __getitem__(self, item):
        return self.A[item]

    def append(self, item):
        if self.capacity:
            pass
        self.capacity = 2 * self.capacity

    def _resize(self, capacity):
        B = self._create_array(2 * capacity)
        for index in range(len(self.A)):
            B[index] = self.A[index]
        self.A = B

    def _create_array(self, cap):
        return ctypes()