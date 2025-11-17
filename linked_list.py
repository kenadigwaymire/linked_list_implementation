class ListNode():
    """ 
    CLASS: ListNode
    Node for a linked list.

    ATTRIBUTES
    ----------
    - val [any type] -> value the node holds
    - next [ListNode] -> node which the ListNode points to

    METHODS
    -------
    - __init__ -> constructor for ListNode object
    - print_val -> prints the value of the node
    - print_next -> prints the value of the next node

    """
    def __init__(self, val = None, next_node = None):
        """
        Constructs a ListNode object.

        ARGUMENTS
        ---------
        - val [any type] -> desired value for node, defaults to None
        - next_node [ListNode] -> node which the constructed node points to, defaults to None

        RETURNS
        -------
        None

        """
        self.val = val
        self.next = next_node

    def print_val(self):
        """
        Prints value of ListNode.

        ARGUMENTS
        ---------
        None

        RETURNS
        -------
        None

        """
        if self.val is None:
            print('Node has None value')
        print(self.val)

    def print_next(self):
        """
        Prints value of next node.

        ARGUMENTS
        ---------
        None

        RETURNS
        -------
        None

        """
        if self.next is None:
            print('Node has no next')
        self.next.print_val()

class LinkedList():
    """
    CLASS: LinkedList
    Implementation of linked list data structure.

    ATTRIBUTES
    ----------
    - head [ListNode] -> start of the linked list
    - length [int] -> number of nodes in the linked list

    METHODS
    -------
    - __init__ -> constructor for LinkedList object
    - calc_length -> calculates length of linked list
    - get -> returns node at a given index
    - print -> prints out values of linked list 
    - insert -> inserts a given node at a given index
    - append -> adds node to end of linked list
    - remove -> removes a given node from linked list
    - idx_remove -> removes node at given index
    - pop -> removes item from end of linked list & returns it

    """

    def __init__(self, head=None):
        """
        Constructs a LinkedList object.

        ARGUMENTS
        ---------
        - head [ListNode] -> start node of linked list, defaults to None

        RETURNS
        -------
        None

        """
        self.head = head
        self.length = self.calc_length()

    def calc_length(self):
        """
        Calculates length of linked list.

        ARGUMENTS
        ---------
        None

        RETURNS
        -------
        - i [int] -> length of linked list

        """
        i = 0
        if not self.head:
            return i
        curr = self.head
        while curr:
            i += 1
            if curr.next:
                curr = curr.next
            else:
                break
        return i

    def get(self, idx):
        """
        Returns item at given index in linked list.

        ARGUMENTS
        ---------
        - idx [int] -> index to grab node at

        RETURNS
        -------
        - curr [ListNode] -> node at given index (None if no such node exists)

        """
        i = 0
        if not self.head:
            print('No nodes in list')
            return None
        curr = self.head
        while i <= idx:
            if i == idx:
                return curr
            curr = curr.next
            i += 1
        print(f'No node at index {idx}')
        return None

    def print(self):
        """
        Prints out values of linked list.

        ARGUMENTS
        ---------
        None

        RETURNS
        -------
        None

        """
        if not self.head:
            print([])
        else:
            curr = self.head
            nodes = [curr.val]
            while curr.next:
                nodes.append(curr.next.val)
                curr = curr.next
            print(nodes)
    
    def insert(self, node, idx):
        """
        Inserts node into linked list at given index. 

        ARGUMENTS
        ---------
        - node [ListNode] -> node to insert
        - idx [int] -> index to insert node at 

        RETURNS
        -------
        None

        """
        # For now, assume node has no next
        if idx == 0:
            old_head = self.head
            self.head = node
            node.next = old_head
            self.length += 1
        elif idx > self.length:
            print(f'Unable to add node {node.val} @ index {idx}')
        else:
            prev_node = self.get(idx-1)
            old_next = prev_node.next
            prev_node.next = node
            node.next = old_next
            self.length += 1
    
    def append(self, node):
        """
        Adds node to end of linked list.

        ARGUMENTS
        ---------
        - node [ListNode] -> node to add

        RETURNS
        -------
        None

        """
        if not self.head:
            self.head = node
        else:
            end_node = self.get(self.length - 1)
            end_node.next = node
        self.length += 1
    
    def remove(self, node):
        """
        Removes given node from linked list.

        ARGUMENTS
        ---------
        - node [ListNode] -> node to remove

        RETURNS
        -------
        None

        """
        if self.head == None:
            print(f'No nodes in list to remove')
        else:
            if self.head == node:
                self.head = self.head.next
                self.length -= 1
            else:
                prev = self.head
                while prev.next:
                    if prev.next == node:
                        if node.next:
                            prev.next = node.next
                        else:
                            prev.next = None
                        self.length -= 1
                        return
                    prev = prev.next
                print(f'Node not found in list')
    
    def idx_remove(self, idx):
        """
        Removes node at given index in linked list

        ARGUMENTS
        ---------
        - idx [int] -> index to remove node at

        RETURNS
        -------
        None

        """
        if self.length == 0:
            print('No nodes in list to remove')
        if idx >= self.length:
            print('Index does not exist in list')
        else:
            if idx == 0:
                self.head = self.head.next
                self.length -= 1
            else:
                prev_node = self.get(idx - 2)
                node_to_remove = prev_node.next
                if node_to_remove.next:
                    prev_node.next = node_to_remove.next
                else:
                    prev_node.next = None
                self.length -= 1

    def pop(self):
        """
        Removes node from end of linked list and returns it.

        ARGUMENTS
        ---------
        None

        RETURNS
        -------
        - last_node [ListNode] -> node at the end of the linked list (None if it doesn't exist)

        """
        if self.length == 0:
            print('No nodes to pop')
            return None
        last_node = self.get(self.length - 1)
        self.idx_remove(self.length - 1)
        self.length -= 1
        return last_node
    
    def delete_list(self):
        """
        Deletes linked list.

        ARGUMENTS
        ---------
        None

        RETURNS
        -------
        None

        """
        self.head = None
        self.length = 0

# Constructing test nodes & list
def make_test_list_1():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_1.next = node_2
    node_2.next = node_3
    return LinkedList(node_1)

# Testing linked list implementation
def main():
    test_list_1 = make_test_list_1()
    test_node = ListNode(4)
    test_node_2 = ListNode(5)
    test_list_1.append(test_node)
    test_list_1.insert(test_node_2, 2)
    test_list_1.print()
    print(test_list_1.length)

if __name__ == '__main__':
    main()
