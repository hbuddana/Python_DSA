def __r_contains(self, current_node, value):
    # Base case: If the current_node is None, the value is not found in the tree.
    if current_node is None:
        return False

    # Check if the current node's value is equal to the target value.
    if value == current_node.value:
        return True

    # If the target value is less than the current node's value,
    # search in the left subtree (values less than the current node's value).
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)

    # If the target value is greater than the current node's value,
    # search in the right subtree (values greater than the current node's value).
    if value > current_node.value:
        return self.__r_contains(current_node.right, value)

def r_contains(self, value):
    # Start the recursive search from the root node.
    return self.__r_contains(self.root, value)


"""
__r_contains is a private recursive helper function that performs binary search on a binary search tree (BST).

The function takes two arguments: current_node, which represents the current node being checked, and value, which is the target value we want to find in the tree.

The base case is when current_node is None, indicating that the target value is not found in the tree, so it returns False.

If the current node's value is equal to the target value, it returns True, indicating that the value is found in the tree.

If the target value is less than the current node's value, it recursively calls __r_contains on the left subtree (values less than the current node's value).

If the target value is greater than the current node's value, it recursively calls __r_contains on the right subtree (values greater than the current node's value)."""



""""
__r_contains(self, current_node, value):

This is a private recursive helper method.
It is responsible for actually performing the binary search within the BST.
It takes two arguments: current_node, which represents the current node being checked during the search, and value, which is the target value we want to find in the tree.
This method is recursive and does the actual work of navigating through the tree to find the target value.

r_contains(self, value):

This is a public method that serves as an interface to initiate the binary search operation.
It takes a single argument, value, which is the value you want to search for in the BST.
This method calls the private recursive helper method __r_contains to start the search from the root of the tree.
The reason for having these two methods is to provide a clean and user-friendly interface for performing searches on the BST while encapsulating the details of the recursive search algorithm within the private helper method. This separation of concerns is a common practice in programming for better code organization and readability.

By having a public method (r_contains) and a private recursive method (__r_contains), you can hide the complexity of the recursive search from the users of the class and ensure that they only need to provide the target value for the search operation. This also allows you to pass the root of the tree as an argument only once when initiating the search, which is more convenient for users."""