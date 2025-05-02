class Solid:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions

    def surface_area(self):
        if self.shape == 'cube':
            a = self.dimensions['a']
            return 6 * a * a
        elif self.shape == 'sphere':
            r = self.dimensions['r']
            return 4 * 3.1416 * r**2

    def volume(self):
        if self.shape == 'cube':
            a = self.dimensions['a']
            return a**3
        elif self.shape == 'sphere':
            r = self.dimensions['r']
            return (4/3) * 3.1416 * r**3
