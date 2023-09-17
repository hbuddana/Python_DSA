# Method to add an edge between two vertices in the graph.
def add_edge(self, v1, v2):
    # Check if both vertices v1 and v2 exist in the adjacency list.
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        # Add v2 to the list of neighbors of v1, and vice versa, creating a bidirectional edge.
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True  # Return True to indicate that the edge was added.
    return False  # Return False if one or both of the vertices don't exist in the graph.
