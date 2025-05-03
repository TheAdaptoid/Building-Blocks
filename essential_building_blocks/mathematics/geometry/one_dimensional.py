from essential_building_blocks.data_structures.lists import Array

DEFAULT_DIMENSIONALITY: int = 3


class Vertex(Array):

    def __init__(self, dimensionality: int = DEFAULT_DIMENSIONALITY):
        super().__init__(size=dimensionality, dtype=float)

        self.__dimensionality: int = dimensionality

    @property
    def dimensionality(self) -> int:
        """
        The dimensionality of the vertex.
        """
        return self.__dimensionality

    def distance(self, other: "Vertex" | None) -> float:
        """
        Calculates the distance between two vertices,
        or from the origin if no other vertex is provided.

        Args:
            other (Vertex | None): The other vertex.

        Returns:
            float: The distance between the two vertices or the distance from the origin.
        """
        if other is None:
            other = Vertex(dimensionality=self.dimensionality)
            for index in range(self.dimensionality):
                other[index] = 0

        if not isinstance(other, Vertex):
            raise TypeError("`other` must be a *Vertex* or None")

        summation: float = 0
        for index in range(self.dimensionality):
            s_value: float = self[index]
            o_value: float = other[index]
            summation += (s_value - o_value) ** 2
        return summation**0.5


class Line:

    def __init__(self, A: Vertex, B: Vertex):
        self.A: Vertex = A
        self.B: Vertex = B

    def is_parallel(self, other: "Line") -> bool:
        """
        Checks if two lines are parallel.

        Args:
            other (Line): The other line.

        Returns:
            bool: True if the lines are parallel, False otherwise.
        """
        raise NotImplementedError

    def midpoint(self) -> Vertex:
        """
        Calculates the midpoint of the line and returns
        a vertex representing the midpoint.

        Returns:
            Vertex: The midpoint of the line.
        """
        raise NotImplementedError

    def intersection(self, line: "Line") -> Vertex | None:
        """
        Calculates the intersection of two lines and returns
        a vertex representing the intersection point.

        Args:
            line (Line): The other line.

        Returns:
            Vertex | None: The intersection point of the two lines.
                None if the lines are parallel.
        """
        raise NotImplementedError

    def bisect(self) -> tuple["Line", "Line", Vertex]:
        """
        Bisects the line into two equal parts.
        Returns a tuple of two lines representing the two equal parts
        of the original line and the midpoint of the original line.

        Returns:
            tuple[Line, Line, Vertex]: A tuple of two lines and a vertex.
        """
        raise NotImplementedError

    def intersect(
        self, other: "Line"
    ) -> tuple["Line", "Line", "Line", "Line", Vertex] | None:
        raise NotImplementedError
