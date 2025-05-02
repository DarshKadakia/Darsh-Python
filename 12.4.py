class Shape:
    def __init__(self, shape, value):
        self.shape = shape
        self.value = value

    def area(self):
        if self.shape == 'square':
            return self.value ** 2
        elif self.shape == 'circle':
            return 3.1416 * self.value ** 2

    def perimeter(self):
        if self.shape == 'square':
            return 4 * self.value
        elif self.shape == 'circle':
            return 2 * 3.1416 * self.value
