# Define a class called 'Graph' to represent an adjacency list graph.
class Graph:
    # Constructor initializes an empty adjacency list.
    def __init__(self):
        self.adj_list = {}

    # Method to print the graph's adjacency list.
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    # Method to add a new vertex to the graph.
    def add_vertex(self, vertex):
        # Check if the vertex is not already in the adjacency list.
        if vertex not in self.adj_list.keys():
            # If not, add the vertex with an empty list as its value (no neighbors yet).
            self.adj_list[vertex] = []
            return True  # Return True to indicate that the vertex was added.
        return False  # Return False to indicate that the vertex already exists.

# Create an instance of the 'Graph' class.
my_graph = Graph()

# Add a vertex 'A' to the graph.
# Note: 'add_vertex' method is used, which returns True if the vertex is added.
vertex_added = my_graph.add_vertex('A')

# Print the graph's adjacency list, which now contains the vertex 'A'.
my_graph.print_graph()
