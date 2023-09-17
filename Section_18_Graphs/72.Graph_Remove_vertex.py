# Method to remove a vertex and its associated edges from the graph.
def remove_vertex(self, vertex):
    # Check if the vertex exists in the adjacency list.
    if vertex in self.adj_list.keys():
        # Iterate through the neighbors of the vertex.
        for other_vertex in self.adj_list[vertex]:
            # For each neighbor, remove the vertex from its list of neighbors.
            self.adj_list[other_vertex].remove(vertex)
        
        # After removing all edges, delete the vertex itself from the adjacency list.
        del self.adj_list[vertex]
        return True  # Return True to indicate that the vertex and its edges were successfully removed.
    
    return False  # Return False if the vertex doesn't exist in the graph.
