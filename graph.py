class Vertex:  # Forward reference
    pass


class Edge:
    pass


class Vertex:
    _idCount = 0
    _list = []

    def __init__(self, position: tuple[int, int]):
        self.id = Vertex._idCount
        self._position = position
        self._edgeList = []
        # self._carQueue = []
        # self._subPriorityCarIndex = 0
        # self._type = None
        # self._vertexColor = None

        Vertex._list.append(self)
        Vertex._idCount += 1
        pass

    def add_edge(self, edge: Edge) -> None:
        self._edgeList.append(edge)


class Edge:
    _idCount = 0
    _list = []

    def __init__(self, vertex1: Vertex, vertex2: Vertex, shape: list):
        raise RuntimeError("Call create_new_edge() instead")

    @classmethod
    def _private_init(cls, vertex1: Vertex, vertex2: Vertex, shape: list[tuple[int, int]]):
        self = cls.__new__(cls)
        self.id = Edge._idCount
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._shape = shape
        return self

    @staticmethod
    def create_new_edge(vertex1: Vertex, vertex2: Vertex, shape: list) -> Edge:
        edge = Edge._private_init(vertex1, vertex2, shape)
        Edge._list.append(edge)
        vertex1.add_edge(edge)
        vertex2.add_edge(edge)
        Edge._idCount += 1
        return edge

    def get_vertex1(self) -> Vertex:
        return self._vertex1

    def get_vertex2(self) -> Vertex:
        return self._vertex2

    def get_shape(self) -> list[tuple[int, int]]:
        return self._shape

    @staticmethod
    def get_edge_list() -> list[Edge]:
        return Edge._list
