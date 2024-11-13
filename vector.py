class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __imul__(self, s):
        """Override *= operator"""
        self.x *= s
        self.y *= s
        self.z *= s
        return self

    def __itruediv__(self, s):
        """Override /= operator"""
        s = 1.0 / s
        self.x *= s
        self.y *= s
        self.z *= s
        return self

    def __mul__(self, s):
        """Override * operator to return a new Vector3D"""
        return Vector(self.x * s, self.y * s, self.z * s)

    def __repr__(self):
        """For easy printing"""
        return f"Vector3D({self.x}, {self.y}, {self.z})"


# Test the functionality
v = Vector(1, 2, 3)
print(f"Original: {v}")

# Using *= operator
v *= 2
print(f"After v *= 2: {v}")

# Using /= operator
v /= 2
print(f"After v /= 2: {v}")

# Using * operator (returns a new Vector3D)
v2 = v * 3
print(f"After v * 3 (new vector): {v2}")

"""
    * (Multiplication): Scales the vector by a scalar and returns a new Vector3D.
    *= (Multiplication Assignment): Scales the vector by a scalar in place.
    /= (Division Assignment): Divides the vector by a scalar in place.
    __repr__: Provides a readable string representation of the Vector3D object.
"""