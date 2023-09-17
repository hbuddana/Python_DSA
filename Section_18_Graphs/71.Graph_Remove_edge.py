# Method to remove an edge between two vertices in the graph.
def remove_edge(self, v1, v2):
    # Check if both vertices v1 and v2 exist in the adjacency list.
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        try:
            # Attempt to remove v2 from the list of neighbors of v1 and vice versa.
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        except ValueError:
            # If the vertices are not connected (edge doesn't exist), ignore the ValueError.
            pass
        return True  # Return True to indicate that the edge removal was attempted.
    return False  # Return False if one or both of the vertices don't exist in the graph.
