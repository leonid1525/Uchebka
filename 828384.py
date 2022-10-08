class Vector:
    def __init__(self, coords=list):
        self.coords=coords
    def __add__(self, other):
        s=Vector([])
        if len(list(self.coords))==len(list(other.coords)):
            for x in range(len(list(self.coords))):
                s.coords.append(self.coords[x]+other.coords[x])
        else:
            raise ValueError(f'left and right lengths differ: {len(list(self.coords))} != {len((list(other.coords)))}')
        return s
    def __mul__(self, other):
        m=0
        if isinstance(other, (Vector)):
            if len(list(self.coords)) == len(list(other.coords)):
                for x in range(len(list(self.coords))):
                    m=m+self.coords[x] * other.coords[x]
                return m
            else:
                raise ValueError(f'left and right lengths differ: {len(list(self.coords))} != {len((list(other.coords)))}')
        if isinstance(other, (int, float)):
            for x in range(len(list(self.coords))):
                self.coords[x]=self.coords[x]*other
            return self
    def __eq__(self, other):
        if self.coords==other.coords:
            return True
        else:
            return False
    def __abs__(self):
        a=0
        for x in range(len(list(self.coords))):
            a=a+(self.coords[x]**2)
        a=a**0.5
        return a
    def __str__(self):
        return (str(self.coords))
print(abs(Vector([17, 2, 3, 8])))