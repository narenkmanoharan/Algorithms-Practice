class Vertex:
    """
    Defining the vertex nodes

    """
    def __init__(self,node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' Adjacent: ' + str([grp.id for grp in self.adjacent])

    def add_neighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight

    def print_map(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    """
    Defining the Graph class

    """
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        vertex = Vertex(node)
        self.vert_dict[node] = vertex
        return vertex

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    x = Graph()
    x.add_vertex('a')
    x.add_vertex('b')
    x.add_vertex('c')
    x.add_vertex('d')
    x.add_vertex('e')
    x.add_edge('a', 'b', 7)
    x.add_edge('a', 'c', 9)
    x.add_edge('a', 'f', 14)
    x.add_edge('b', 'c', 10)
    x.add_edge('b', 'd', 15)
    x.add_edge('c', 'd', 11)
    x.add_edge('c', 'f', 2)
    x.add_edge('d', 'e', 6)
    x.add_edge('e', 'f', 9)

    for v in x:
        for w in v.print_map():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    for v in x:
        print('x.vert_dict[%s] = %s' %(v.get_id(), x.vert_dict[v.get_id()]))
