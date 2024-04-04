# How to use
from visualize.visualize import Visualize, Color
from graph import Edge, Vertex

a = Vertex((100, 100))
b = Vertex((400, 200))
c = Vertex((200, 300))
d = Vertex((310, 40))

Edge.create_new_edge(a, b, [])
Edge.create_new_edge(a, c, [])
Edge.create_new_edge(d, c, [])


Visualize.init(600, 600, "Traffic Manager", 10)

while True:
    Visualize.before_update()
    if not Visualize.is_running:
        break

    vertex: Vertex
    for index, vertex in enumerate(Vertex._list):
        Visualize.draw_rect(Visualize.get_color(
            index), vertex._position + (30, 30))

    edge: Edge
    for index, edge in enumerate(Edge._list):
        Visualize.draw_line(Color.BLACK, edge.get_vertex1(
        )._position, edge.get_vertex2()._position, 10)

    Visualize.after_update()
