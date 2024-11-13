class Vector:
    def __init__(self, a=0.0, b=0.0, c=0.0):
        self.x = a
        self.y = b
        self.z = c

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        elif i == 2:
            return self.z
        else:
            raise IndexError("Index out of range for Vector3D")

    def __setitem__(self, i, value):
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value
        elif i == 2:
            self.z = value
        else:
            raise IndexError("Index out of range for Vector3D")


""" Example usage
v = Vector(1.0, 2.0, 3.0)
print(v[0])  # Accessing x
v[1] = 4.0  # Modifying y
print(v[1])  # Accessing updated y
"""