from linear_algebra import Vector

DEFAULT_DIMENSIONALITY: int = 3


class Point(Vector):
    """A point in n-dimensional space."""

    def __init__(self, dimensionality: int = DEFAULT_DIMENSIONALITY):
        if dimensionality < 1:
            raise ValueError("Dimensionality must be at least 1.")

        self.dimensionality: int = dimensionality
        self.component_vector: Vector = Vector(dimensionality)

    def change_dimensionality(self, n: int) -> None:
        """
        Change the dimensionality of the point.
        This will resize the component vector to the new dimensionality.
        Components beyond the original dimensionality will be set to 0.0.
        If the new dimensionality is less than the original,
        the excess components will be discarded.

        Args:
            n (int): The new dimensionality.
        """
        if n < 1:
            raise ValueError("Dimensionality must be at least 1.")

        if n == self.dimensionality:
            return

        new_vector: Vector = Vector(n)
        new_vector[: self.dimensionality] = self.component_vector[: self.dimensionality]
        new_vector[self.dimensionality :] = 0.0

        self.dimensionality = n

    def __getitem__(self, index: int) -> float:
        return self.component_vector[index]

    def __setitem__(self, index: int, value: float) -> None:
        self.component_vector[index] = value
